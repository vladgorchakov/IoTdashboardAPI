from django.contrib import admin
from dashboard.models import Measure, Place, Sensor, Monitoring


admin.site.register(Measure)
admin.site.register(Place)
admin.site.register(Sensor)
admin.site.register(Monitoring)
