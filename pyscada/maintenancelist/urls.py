from django.urls import path
from . import views

urlpatterns = [
    path("view/<link_title>/device/<device_id>", views.device_informations, name="device-informations"),
]