from django.urls import path

from application.views import MonitoringRequestCreate

urlpatterns = [
    path('', MonitoringRequestCreate.as_view(), name='monitoring_request_view'),
]
