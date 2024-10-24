from django.urls import path

from . import views

app_name = "plants"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:plant_id>/", views.detail, name="detail")
]
