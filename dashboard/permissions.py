from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission
from dashboard.models import Sensor


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):

        return request.user == obj.user


class IsSensorOwner(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            sensor_id = request.data.get('sensor', None)
            if sensor_id:
                try:
                    return request.user == Sensor.objects.get(pk=sensor_id).user
                except ObjectDoesNotExist:
                    return False

        return False
