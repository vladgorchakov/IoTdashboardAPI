from rest_framework import serializers
from dashboard.models import Place, Measure, Sensor, Monitoring


class PlaceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = ('id', 'title')


class PlaceCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Place
        fields = '__all__'


class PlaceDetailSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='id', read_only=True)

    class Meta:
        model = Place
        fields = '__all__'


class MeasureListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'id')
        model = Measure


class MeasureDetailSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Measure
        fields = '__all__'


class MeasureCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Measure
        fields = '__all__'


class SensorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'title',)


class SensorCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Sensor
        fields = '__all__'


class SensorDetailSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Sensor
        fields = '__all__'


class MonitoringListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Monitoring
        fields = ('id', 'sensor', 'measure', 'value',)


class MonitoringCreateSerializer(MonitoringListSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Monitoring
        fields = ('sensor', 'measure', 'value')


class MonitoringDetailSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(slug_field='id', read_only=True)

    class Meta:
        model = Monitoring
        fields = '__all__'
