# syntax=docker/dockerfile:1

# --- Frontend: npm packages + compiled site.css -------------------------------
FROM node:24-alpine AS assets
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --no-audit --no-fund
COPY senne/templates/assets ./senne/templates/assets
RUN npm run build && npm prune --omit=dev

# --- Python app ---------------------------------------------------------------
FROM python:3.13-slim AS app
COPY --from=ghcr.io/astral-sh/uv:0.12 /uv /usr/local/bin/uv

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/opt/venv \
    PATH=/opt/venv/bin:$PATH

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv uv sync --locked --no-dev --no-install-project

COPY . .
COPY --from=assets /app/node_modules ./node_modules
COPY --from=assets /app/senne/templates/assets/css/site.css ./senne/templates/assets/css/site.css
RUN SECRET_KEY=collectstatic-only python manage.py collectstatic --noinput \
    && useradd --uid 1000 --no-create-home --shell /usr/sbin/nologin app

USER 1000:1000
EXPOSE 8000
# One process, four threads (gthread): fits the memory budget, a slow thumbnail
# render does not block the other requests.
CMD ["gunicorn", "senne.wsgi", "--bind", "0.0.0.0:8000", "--workers", "1", "--threads", "4", \
     "--no-control-socket", "--access-logfile", "-"]
