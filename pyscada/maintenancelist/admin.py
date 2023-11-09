from pyscada.admin import admin_site
from .models import MaintenanceDevice, MaintenanceDeviceType

admin_site.register(MaintenanceDevice)
admin_site.register(MaintenanceDeviceType)