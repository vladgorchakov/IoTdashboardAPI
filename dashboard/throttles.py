from rest_framework import throttling


class UserMonitoringCreateRateThrottle(throttling.UserRateThrottle):
    rate = '120/minute'
    def allow_request(self, request, view):


class UserMonitoringRateThrottle(throttling.UserRateThrottle):
    rate = '1000/minute'
