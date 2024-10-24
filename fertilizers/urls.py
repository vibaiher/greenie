from django.urls import path

from . import views

app_name = "fertilizers"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:fertilizer_id>/", views.detail, name="detail")
]
