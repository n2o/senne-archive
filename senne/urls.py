from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views as flatpages
from django.urls import include, path, re_path
from django.views.generic import RedirectView

from archive import views as archive_views
from frontpage import views


def page(request, slug):
    # Flatpages keep their stored "/impressum/" URL; publicly they live at /impressum.
    return flatpages.flatpage(request, f"/{slug}/")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin", RedirectView.as_view(pattern_name="admin:index")),
    path("", include("archive.urls")),
    path("", views.index, name="index"),
]

if settings.S3_BUCKET:
    urlpatterns += [path("media/<path:name>", archive_views.media)]
elif settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path("<slug:slug>", page, name="pages"),
    # Links without clutter: /archiv/ -> /archiv (old and external links), query string kept.
    # rest never starts with / or \, else //evil.com/ would redirect off-site.
    re_path(
        r"^(?P<rest>[^/\\](?:.*[^/])?)/$", RedirectView.as_view(url="/%(rest)s", permanent=True, query_string=True)
    ),
]
