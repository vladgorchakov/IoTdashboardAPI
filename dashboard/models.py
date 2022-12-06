from django.contrib.auth.models import User
from django.db import models


class DataTimeModelMixin(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TitleDescriptionModelMixin(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        abstract = True


class Measure(TitleDescriptionModelMixin, DataTimeModelMixin):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Place(TitleDescriptionModelMixin, DataTimeModelMixin):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.user}'


class Sensor(TitleDescriptionModelMixin, DataTimeModelMixin):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    place = models.ForeignKey(to=Place, on_delete=models.SET_NULL, blank=True, null=True)
    measure = models.ManyToManyField(to=Measure)

    def __str__(self):
        return f'{self.title} - {self.user}'


class Monitoring(DataTimeModelMixin):
    sensor = models.ForeignKey(to=Sensor, on_delete=models.CASCADE)
    measure = models.ForeignKey(to=Measure, on_delete=models.CASCADE, null=True, blank=True)
    value = models.FloatField()

    def __str__(self):
        return f'{self.sensor} ({self.measure})'
