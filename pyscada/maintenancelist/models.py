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

class MaintenanceDevice(WidgetContentModel):

    id = models.AutoField(primary_key=True)
    reference = models.CharField(verbose_name="Reference", max_length=50, blank=True, null=True)
    name = models.CharField(verbose_name="Title", max_length=100)
    type = models.CharField(verbose_name="Type of device", max_length=50)
    createdAt = models.DateTimeField(verbose_name="Created at", default=datetime.datetime.now)
    updatedAt = models.TextField(verbose_name="Updated at", default=datetime.datetime.now, blank=True, null=True)
    period = models.CharField(verbose_name="Select maintenance period", choices=maintenance_period_choices, max_length=50)
    lastMaintenance = models.DateTimeField(verbose_name="Date last maintenance", blank=True, null=True)
    isConform = models.BooleanField(verbose_name="Device is conform after control", blank=False, null=False)
    maintainer = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    report = models.CharField(verbose_name="report url join", blank=True, null=True)
    

    def __str__(self):
        return self.title + "_" + self.type + "_" + str(self.id)
    

    def gen_html(self, **kwargs):
        """
        : return main template for energy display object
        """
        # energy displayer template is templates folder
        main_template = get_template("maintenance-list.html")
        main_content = None
        main_content = main_template.render(
            dict(
                uuid=uuid4().hex,
                item=self,
            )
        )
        opts = dict()
        opts["flot"] = False
        opts["show_daterangepicker"] = True
        opts["show_timeline"] = True
        opts["object_config_list"] = set()
        opts["javascript_files_list"] = [STATIC_URL + "pyscada/js/maintenance-list.js",]
        opts["css_files_list"] = [STATIC_URL + "pyscada/css/maintenance-list.css",]

        return main_content, None, opts
