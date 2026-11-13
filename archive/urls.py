from django.urls import path

from . import views

app_name = "archive"
urlpatterns = [
    path("archiv/<int:pk>", views.detail, name="details"),
    path("archiv", views.index, name="index"),
]
