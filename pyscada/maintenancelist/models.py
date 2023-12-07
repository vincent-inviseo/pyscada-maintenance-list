# -*- coding: utf-8 -*-
import datetime
from uuid import uuid4
from pyscada.hmi.models import WidgetContentModel
from pyscada.models import User
from django.conf import settings
STATIC_URL = str(settings.STATIC_URL) if hasattr(settings, "STATIC_URL") else "static"

from django.template.loader import get_template
from django.db import models

maintenance_period_choices = (
    ("every month", "every month"),
    ("each 3 months", "each 3 months"),
    ("each 4 months", "each 4 months"),
    ("each year", "each year"),
    ("every 2 years", "every 2 years")
)

class MaintenanceDeviceType(models.Model):
    
    id = models.AutoField(primary_key=True)
    type = models.CharField(verbose_name="Type of device", max_length=50)
    
    def __str__(self):
        return self.type


class MaintenanceDevice(models.Model):

    id = models.AutoField(primary_key=True)
    reference = models.CharField(verbose_name="Réference", max_length=50, blank=True, null=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    type = models.ForeignKey(MaintenanceDeviceType, on_delete=models.DO_NOTHING, null=True, blank=True,)
    createdAt = models.DateTimeField(verbose_name="Created at", default=datetime.datetime.now)
    updatedAt = models.DateTimeField(verbose_name="Updated at", default=datetime.datetime.now, blank=True, null=True)
    period = models.CharField(verbose_name="Select maintenance period", choices=maintenance_period_choices, max_length=50)
    
    class Meta:
        ordering = ["-createdAt"]
    

    def __str__(self):
        return self.name
    


class Maintenance(models.Model):
    
    id = models.AutoField(primary_key=True)
    makedAt = models.DateTimeField(verbose_name="Make at", default=datetime.datetime.now)
    isConform = models.BooleanField(verbose_name="Device is conform after control", blank=False, null=False)
    maintainer = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    report = models.CharField(verbose_name="report url join", blank=True, null=True, max_length=150)
    maintenanceDevice = models.ForeignKey(MaintenanceDevice, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["-makedAt"]
    

    def __str__(self):
        return self.maintenanceDevice.name + "-" + self.makedAt.date().strftime(format="%Y-%m-%d")
    

class MaintenanceWidgetContent(WidgetContentModel):
    
    id = models.AutoField(primary_key=True)
    
    def gen_html(self, **kwargs):
        """
        : return main template for energy display object
        """
        # energy displayer template is templates folder
        main_template = get_template("maintenance-list.html")
        main_content = None
        main_content = main_template.render(
            dict(
                devices=MaintenanceDevice.objects.all()
            )
        )
        opts = dict()
        opts["show_daterangepicker"] = False
        opts["show_timeline"] = False
        opts["object_config_list"] = set()
        opts["javascript_files_list"] = [STATIC_URL + "pyscada/js/maintenance-list.js",]
        opts["css_files_list"] = [STATIC_URL + "pyscada/css/maintenance-list.css",]

        return main_content, None, opts
    
    def __str__(self):
        return "Liste de maintenance"