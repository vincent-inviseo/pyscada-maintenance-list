from django.urls import path
from . import views

urlpatterns = [
    path("maintenance-list/", views.view_maintenance, name="view_maintenance"),
]