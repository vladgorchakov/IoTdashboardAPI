from rest_framework import viewsets
from dashboard.models import Place, Measure, Sensor, Monitoring
from dashboard.serializers import PlaceDetailSerializer, MeasureCreateSerializer, SensorListSerializer, \
    MonitoringCreateSerializer, PlaceListSerializer, PlaceCreateSerializer, MeasureListSerializer, \
    MeasureDetailSerializer, SensorDetailSerializer, SensorCreateSerializer, MonitoringListSerializer, \
    MonitoringDetailSerializer


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


class MonitorinDetailSerializer:
    pass


class MonitoringViewSet(viewsets.ModelViewSet):
    queryset = Monitoring.objects.order_by('-update_time')
    serializer_class = MonitoringCreateSerializer

    def get_queryset(self):
        print(self.request.user)
        queryset = Monitoring.objects.select_related('sensor').filter(sensor__user=self.request.user)
        return queryset

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return MonitoringListSerializer
            case 'create':
                return MonitoringCreateSerializer

        return MonitoringDetailSerializer
