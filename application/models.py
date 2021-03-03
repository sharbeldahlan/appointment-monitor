from django.db import models

from application.constants import OFFICE_CHOICES
from application.constants import SERVICE_CHOICES


class MonitoringRequest(models.Model):
    """
    Object to contain the details of the monitoring request.
    """
    # Appointment service type chosen by the user.
    # From the value of this field, we will use mappings in constants.py to get
    # the actual booking page's "Category" and "Service".
    service_choice = models.CharField(choices=SERVICE_CHOICES, max_length=55)
    # Migri office location chosen for the Appointment.
    office_choice = models.CharField(choices=OFFICE_CHOICES, max_length=55)
    # Email address to which an email with the available appointment details is sent.
    to_email = models.EmailField(max_length=254)
