import json
import time
from pyscada.hmi.models import GroupDisplayPermission
from pyscada.utils import get_group_display_permission_list
from pyscada.hmi.models import View
from pyscada.core import version as core_version
import traceback
import pyscada.hmi.models
from pyscada.models import RecordedData, VariableProperty, Variable, Device
from pyscada.models import Log
from pyscada.models import DeviceWriteTask, DeviceReadTask
from pyscada.hmi.models import ControlItem
from pyscada.hmi.models import Form
from pyscada.hmi.models import GroupDisplayPermission
from pyscada.hmi.models import Widget
from pyscada.hmi.models import CustomHTMLPanel
from pyscada.hmi.models import Chart
from pyscada.hmi.models import View
from pyscada.hmi.models import ProcessFlowDiagram
from pyscada.hmi.models import Pie
from pyscada.hmi.models import Page
from pyscada.hmi.models import SlidingPanelMenu
from pyscada.utils import gen_hiddenConfigHtml, get_group_display_permission_list

from django.conf import settings
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.decorators.csrf import requires_csrf_token
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.db.models.fields.related import OneToOneRel

import time
import json
import logging

from .models import MaintenanceDevice


def view_maintenance(request):
    devices = MaintenanceDevice.objects.all()
    context = {
        "devices": devices
    }
    return TemplateResponse(request, "maintenance-list.html", context)