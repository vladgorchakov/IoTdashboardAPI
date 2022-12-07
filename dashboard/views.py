from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from dashboard.models import Place, Measure, Sensor, Monitoring
from dashboard.permissions import IsAuthor, IsSensorOwner
from dashboard.serializers import PlaceDetailSerializer, MeasureCreateSerializer, SensorListSerializer, \
    MonitoringCreateSerializer, PlaceListSerializer, PlaceCreateSerializer, MeasureListSerializer, \
    MeasureDetailSerializer, SensorDetailSerializer, SensorCreateSerializer, MonitoringListSerializer, \
    MonitoringDetailSerializer
from dashboard.throttls import UserMonitoringRateThrottle, UserMonitoringCreateRateThrottle


class PlaceViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Place.objects.filter(user=self.request.user).order_by('-update_time')

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return PlaceListSerializer
            case 'create':
                return PlaceCreateSerializer
        return PlaceDetailSerializer

    # def get_permissions(self):
    #     permissions = [IsAuthenticated]
    #     if self.action in ('retrieve', 'update', 'delete'):
    #         permissions.append(IsAuthor)
    #
    #     return [permission() for permission in permissions]


class MeasureViewSet(viewsets.ModelViewSet):
    serializer_class = MeasureCreateSerializer

    def get_queryset(self):
        return Measure.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return MeasureListSerializer
            case 'create':
                return MeasureCreateSerializer
        return MeasureDetailSerializer


class SensorViewSet(viewsets.ModelViewSet):
    serializer_class = SensorListSerializer

    def get_queryset(self):
        return Sensor.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return SensorListSerializer
            case 'create':
                return SensorCreateSerializer

        return SensorDetailSerializer


class MonitoringViewSet(viewsets.ModelViewSet):
    throttle_classes = [UserMonitoringRateThrottle]

    def get_queryset(self):
        queryset = Monitoring.objects.select_related('sensor').filter(sensor__user=self.request.user)
        return queryset.order_by('-update_time')

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return MonitoringListSerializer
            case 'create':
                return MonitoringCreateSerializer

        return MonitoringDetailSerializer

    def get_permissions(self):
        permissions = [IsAuthenticated]
        if self.action == 'create':
            permissions.append(IsSensorOwner)

        return [permission() for permission in permissions]

    def get_throttles(self):
        if self.action == 'create':
            throttle_classes = [UserMonitoringCreateRateThrottle]
        else:
            throttle_classes = [UserMonitoringRateThrottle]

        return [throttle() for throttle in throttle_classes]
