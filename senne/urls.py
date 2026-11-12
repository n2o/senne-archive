from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views as flatpages
from django.urls import include, path

from archive import views as archive_views
from frontpage import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("archiv/", include("archive.urls")),
    path("", views.index, name="index"),
]

if settings.S3_BUCKET:
    urlpatterns += [path("media/<path:name>", archive_views.media)]
elif settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [path("<path:url>", flatpages.flatpage, name="pages")]
