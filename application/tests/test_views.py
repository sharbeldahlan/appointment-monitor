import pytest
from django.test import RequestFactory
from django.urls import reverse

from application.views import MonitoringRequestCreate


@pytest.fixture()
def valid_data_post_response():
    """ Fixture for response of monitoring_request_view when posted with valid data """
    factory = RequestFactory()
    url = reverse('monitoring_request_view')
    data = {
        'service_choice': 'citizenship_application',
        'office_choice': 'Helsinki Käenkuja',
        'to_email': 'test@example.com'
    }
    request = factory.post(path=url, data=data)
    response = MonitoringRequestCreate.as_view()(request)
    yield response


def test_monitoring_request_view__get__returns_200():
    """ Test the response of a GET request to the MonitoringRequestCreate view """
    factory = RequestFactory()
    url = reverse('monitoring_request_view')
    request = factory.get(url)
    response = MonitoringRequestCreate.as_view()(request)
    assert response.status_code == 200


def test_monitoring_request_view__post__valid_data__response_as_expected(valid_data_post_response):
    assert valid_data_post_response.status_code == 200

# TODO: Test posting to the view with invalid data

