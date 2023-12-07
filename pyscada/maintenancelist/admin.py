from pyscada.admin import admin_site
from .models import MaintenanceDevice, MaintenanceDeviceType, Maintenance

admin_site.register(MaintenanceDevice)
admin_site.register(MaintenanceDeviceType)
admin_site.register(Maintenance)