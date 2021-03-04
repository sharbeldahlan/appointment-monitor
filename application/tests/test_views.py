from django.test import RequestFactory
from django.urls import reverse

from application.views import MonitoringRequestCreate


# TODO: Add fixture for post response of MonitoringRequestCreate view, after posting with some data


def test_monitoring_request_view__get__returns_200():
    """ Test the response of a GET request to the MonitoringRequestCreate view """
    factory = RequestFactory()
    url = reverse('monitoring_request_view')
    request = factory.get(url)
    response = MonitoringRequestCreate.as_view()(request)
    assert response.status_code == 200


# TODO: Test posting to the view with valid data

# TODO: Test posting to the view with invalid data

