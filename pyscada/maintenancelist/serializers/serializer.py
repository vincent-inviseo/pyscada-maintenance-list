import logging
from django.core.serializers import serialize

def maintenance_device_serializer(instance):
    return {
        "id": instance.id,
        "reference": instance.reference,
        "name": instance.name,
        "type": instance.type,
        "createdAt": instance.createdAt,
        "updatedAt": instance.updateAt,
        "period": instance.period
        }

def maintenance_serializer(instance):
    return {
        "id": instance.id,
        "makedAt": instance.makedAt,
        "isConform": instance.isConform,
        "maintainer": instance.maintainer,
        "report":instance.report,
        "maintenanceDevice":instance.maintenanceDevice
    }

def maintenance_device_type_serialized(instance):
    return {
        'id': instance.id,
        'type': instance.type,
    }