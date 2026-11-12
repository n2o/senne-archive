from django.urls import path

from . import views

app_name = "archive"
urlpatterns = [
    path("<int:pk>", views.detail, name="details"),
    path("", views.index, name="index"),
]
