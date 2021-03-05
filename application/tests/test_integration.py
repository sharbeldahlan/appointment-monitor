from unittest.mock import call
from unittest.mock import patch

import pytest

from application.constants import CITIZENSHIP_APPLICATION
from application.constants import HELSINKI_MALMI
from application.constants import LAHTI
from application.constants import RESIDENCE_PERMIT_SERVICE_PERMANENT
from application.models import MonitoringRequest
from application.services import monitoring_service


@pytest.fixture()
def monitoring_request():
    """ Fixture for monitoring_request object created with sample data """
    monitoring_request = MonitoringRequest.objects.create(
        service_choice=CITIZENSHIP_APPLICATION,
        office_choice=LAHTI,
        to_email='test@example.com'
    )
    yield monitoring_request
    # Teardown: delete the object at the end of the test.
    monitoring_request.delete()


@pytest.mark.django_db()
@patch('application.services.scrape_booking_site')
def test_service_integration__no_monitoring_request_objects__no_calls_for_scraping(
        mock_scrape_booking_site, monitoring_request):
    """
    Test that, when the monitoring_service() is run with a one monitoring_request object in the database,
    The service will call scrape_booking_site() once with the correct parameters.
    """
    monitoring_service()

    # Scrape_booking_site() will be called with the "display" version office_choice, which is obtained by django's
    # get_office_choice_display() built-in method for models. In other words:
    # monitoring_request.office_choice = "lahti", but "Lahti" will be passed to scrape_booking_site()
    assert mock_scrape_booking_site.call_args == call(service_choice=CITIZENSHIP_APPLICATION, office_choice='Lahti')


@pytest.mark.django_db()
@patch('application.services.scrape_booking_site')
def test_service_integration__two_monitoring_request_objects__two_calls_for_scraping(
        mock_scrape_booking_site, monitoring_request):
    """
    Test that, when there are more than one monitoring_request objects in the database,
    The service will call scrape_booking_site() once for each object.
    """
    # One monitoring request object created from the fixture, and another one here:
    MonitoringRequest.objects.create(
        service_choice=RESIDENCE_PERMIT_SERVICE_PERMANENT,
        office_choice=HELSINKI_MALMI,
        to_email='test@example.com'
    )
    monitoring_service()

    # scrape_booking_site() will be called twice
    assert mock_scrape_booking_site.call_count == 2
    assert mock_scrape_booking_site.call_args_list == [
        call(office_choice='Lahti', service_choice='citizenship_application'),
        call(office_choice='Helsinki : Malmi', service_choice='Permanent')
    ]
