import logging
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from .models import MaintenanceDevice, Maintenance


logger = logging.getLogger(__name__)

UNAUTHENTICATED_REDIRECT = (
    settings.UNAUTHENTICATED_REDIRECT
    if hasattr(settings, "UNAUTHENTICATED_REDIRECT")
    else "/accounts/login/"
)


def unauthenticated_redirect(func):
    def wrapper(*args, **kwargs):
        if not args[0].user.is_authenticated:
            return redirect("%s?next=%s" % (UNAUTHENTICATED_REDIRECT, args[0].path))
        return func(*args, **kwargs)

    return wrapper


def device_informations(request, device_id):
    device = MaintenanceDevice.objects.get(pk=device_id)
    maintenances = Maintenance.objects.filter(maintenanceDevice_id=device_id)
    fields = device._meta.get_fields() 
    
    # Initialisation des listes pour les filtres
    seen_references = list({device.reference for device in MaintenanceDevice.objects.all()})
    seen_types = list({device.type for device in MaintenanceDevice.objects.all()})
    seen_periods = list({device.period for device in MaintenanceDevice.objects.all()})
    
    context={
        "device": device,
        "maintenances": maintenances
    }
    
    return TemplateResponse(request, 'device-maintenance-list.html', context)