# sennearchiv.de

Digitales Archiv der Naturschutz-Stiftung Senne. Django 5.2 LTS, Bootstrap 4.

- **Hosting:** schnaq-Cluster (Scaleway Kapsule) via ArgoCD, Chart `charts/sennearchiv` in `schnaq/charts`
- **Daten:** Postgres (Scaleway `pg0`, DB `sennearchiv`)
- **Dateien:** privater S3-Bucket `sennearchiv` (Scaleway-Projekt „Sennearchiv“), ausgeliefert über signierte URLs
- **Statics:** im Image gebaut, ausgeliefert von WhiteNoise
- **Image:** `ghcr.io/n2o/senne-archive:sha-<commit>`, gebaut von GitHub Actions bei jedem Push auf `master`

## Lokal entwickeln

```sh
npm ci && npm run build          # Frontend-Pakete + site.css
uv sync
export SECRET_KEY=dev DEBUG=true # ohne DATABASE_URL/S3_BUCKET: SQLite + Dateien in ./media
uv run python manage.py migrate
uv run python manage.py runserver
```

Konfiguration ausschließlich über Umgebungsvariablen, siehe Kopf von `senne/settings.py`.

## Checks (wie in CI)

```sh
uv run ruff check .
uv run python manage.py check --deploy --fail-level WARNING   # braucht einen ≥50 Zeichen langen SECRET_KEY
uv run python manage.py makemigrations --check --dry-run
uv run python manage.py test
```

## Deployment

Neues Image-Tag in `charts/sennearchiv/values.yaml` (Repo `schnaq/charts`) eintragen und mergen;
ArgoCD rollt aus, Migrationen laufen als initContainer. Umzug vom alten Server und Datenimport:
`charts/sennearchiv/README.md` und `scripts/prod_fixture.py`.
