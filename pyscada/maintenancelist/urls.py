from django.urls import path
from . import views

urlpatterns = [
    path("maintenancelist/device/<device_id>", views.device_informations, name="device-informations"),
]