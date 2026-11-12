"""
Django settings for sennearchiv.de.

All deployment-specific values come from environment variables:

  SECRET_KEY            required (no fallback, the repository is public)
  DEBUG                 "true" enables debug mode, default off
  ALLOWED_HOSTS         comma-separated, default "sennearchiv.de,www.sennearchiv.de"
  DATABASE_URL          e.g. postgres://user:pass@host:5432/sennearchiv?sslmode=require,
                        default: local SQLite (development only)
  S3_BUCKET             media bucket; unset → media on local disk (development only)
  S3_ENDPOINT_URL       default https://s3.nl-ams.scw.cloud
  S3_REGION             default nl-ams
  AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY   read by boto3 directly
"""

import os
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = os.environ.get("DEBUG", "false").lower() == "true"
ALLOWED_HOSTS = [
    h.strip() for h in os.environ.get("ALLOWED_HOSTS", "sennearchiv.de,www.sennearchiv.de").split(",") if h.strip()
]
if DEBUG:
    ALLOWED_HOSTS += ["localhost", "127.0.0.1"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "django.contrib.messages",
    "django.contrib.flatpages",
    "senne",
    "archive",
    "frontpage",
    "pagedown",
    "reversion",
    "sorl.thumbnail",
]

MIDDLEWARE = [
    "senne.health.healthz",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "senne.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "senne.wsgi.application"

DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}", conn_max_age=600, conn_health_checks=True
    ),
}
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", "OPTIONS": {"min_length": 12}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "de-de"
TIME_ZONE = "Europe/Berlin"
USE_I18N = True
USE_TZ = True

SITE_ID = 1

# Static files: built into the image (collectstatic) and served by WhiteNoise.
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
# Only the dist folders of the npm packages, under their usual paths.
NPM_DIRS = ("bootstrap/dist", "jquery/dist", "lightbox2/dist", "select2/dist", "font-awesome/css", "font-awesome/fonts")
STATICFILES_DIRS = [(d, BASE_DIR / "node_modules" / d) for d in NPM_DIRS] + [BASE_DIR / "senne/templates/assets"]
WHITENOISE_KEEP_ONLY_HASHED_FILES = True

# Media: private S3 bucket, files are delivered through short-lived signed URLs.
# This also keeps attachments of non-public archive items unreachable.
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
S3_BUCKET = os.environ.get("S3_BUCKET")
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}
if S3_BUCKET:
    STORAGES["default"] = {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": S3_BUCKET,
            "endpoint_url": os.environ.get("S3_ENDPOINT_URL", "https://s3.nl-ams.scw.cloud"),
            "region_name": os.environ.get("S3_REGION", "nl-ams"),
            "default_acl": "private",
            "file_overwrite": False,
            "signature_version": "s3v4",
            "addressing_style": "virtual",
        },
    }

# Behind ingress-nginx / Cloudflare: TLS terminates upstream.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# HSTS preload would commit the domain to browser lists; not wanted.
SILENCED_SYSTEM_CHECKS = ["security.W021"]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "INFO"},
}
