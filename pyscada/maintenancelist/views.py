import logging
from django.conf import settings
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from .models import MaintenanceDevice, Maintenance
from pyscada.hmi.models import Page

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


@unauthenticated_redirect
def device_informations(request, device_id, link_title):
    
    device = MaintenanceDevice.objects.get(pk=device_id)
    maintenances = Maintenance.objects.filter(maintenanceDevice_id=device_id)
    fields = device._meta.get_fields() 
    
    page_list = Page.objects.all()
    
    context={
        "device": device,
        "maintenances": maintenances,
        "fields": fields,
        "page_list": page_list,
        "link_title": link_title
    }
    
    return TemplateResponse(
        request, "device-maintenance-list.html", context=context
    )
    
    