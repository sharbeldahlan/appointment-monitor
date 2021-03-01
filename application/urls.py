from django.urls import path

from application.views import MonitoringRequestView

urlpatterns = [
    path('', MonitoringRequestView.as_view, name='monitoring_request_view'),
]
