from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from application.models import MonitoringRequest


class MonitoringRequestCreate(SuccessMessageMixin, CreateView):
    """
    View to create MonitoringRequest object.
    Upon success, the view redirects to itself.
    """
    model = MonitoringRequest
    fields = ['service_choice', 'office_choice', 'to_email']
    success_url = reverse_lazy('monitoring_request_view')
    success_message = "Appointment monitoring request taken. We're on it! 🦾"
