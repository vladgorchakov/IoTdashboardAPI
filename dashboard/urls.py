from rest_framework import routers
from dashboard.views import PlaceViewSet, MeasureViewSet, SensorViewSet, MonitoringViewSet

router = routers.DefaultRouter()
router.register(prefix='places', viewset=PlaceViewSet, basename='places')
router.register(prefix='measures', viewset=MeasureViewSet, basename='measures')
router.register(prefix='sensors', viewset=SensorViewSet, basename='sensors')
router.register(prefix='monitoring', viewset=MonitoringViewSet, basename='monitoring')

urlpatterns = router.urls
