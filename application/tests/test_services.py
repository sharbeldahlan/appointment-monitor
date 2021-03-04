from unittest.mock import call
from unittest.mock import patch

import pytest

from application.services import monitoring_service


@pytest.fixture()
def mock_monitoring_request_object():
    """ Fixture for monitoring_request object created with sample data """
    class MockMonitoringRequest:
        service_choice = 'citizenship_application'
        office_choice = 'helsinki'
        to_email = 'test@example.com'

        @staticmethod
        def get_office_choice_display():
            return 'Helsinki'

    yield MockMonitoringRequest()


@patch('application.services.send_email')
@patch('application.services.scrape_booking_site')
@patch('application.services.MonitoringRequest.objects')
def test_monitoring_service__no_available_appointment(mock_objects,
                                                      mock_scrape_booking_site,
                                                      mock_send_email,
                                                      mock_monitoring_request_object):
    """ Test to check the branch when scrape_booking_site() returns none """
    # Simulate that getting all MonitoringRequest objects gets us the
    # mock_monitoring_request_object in the fixture
    mock_objects.all.return_value = [mock_monitoring_request_object]

    # Simulate no available appointment (available_appointment = None)
    mock_scrape_booking_site.return_value = None

    # Run the monitoring service
    monitoring_service()

    assert mock_scrape_booking_site.call_args == call(
        service_choice='citizenship_application',
        office_choice='Helsinki',
    )
    assert mock_send_email.call_count == 0


@patch('application.services.send_email')
@patch('application.services.scrape_booking_site')
@patch('application.services.MonitoringRequest.objects')
def test_monitoring_service__available_appointment(mock_objects,
                                                   mock_scrape_booking_site,
                                                   mock_send_email,
                                                   mock_monitoring_request_object):
    """ Test to check the branch when scrape_booking_site() returns something """
    # Simulate that getting all MonitoringRequest objects gets us the
    # mock_monitoring_request_object in the fixture
    mock_objects.all.return_value = [mock_monitoring_request_object]

    # Simulate an available appointment
    available_appointment = {
        'available_time': '8:45',
        'date': '26.02'
    }
    mock_scrape_booking_site.return_value = available_appointment

    # Run the monitoring service
    monitoring_service()

    assert mock_scrape_booking_site.call_args == call(
        service_choice='citizenship_application',
        office_choice='Helsinki',
    )
    assert mock_send_email.call_args == call(
        available_appointment=available_appointment,
        to_email='test@example.com',
    )


@patch('application.services.send_email')
@patch('application.services.scrape_booking_site')
@patch('application.services.MonitoringRequest.objects')
def test_monitoring_service__no_monitoring_requests_in_database(mock_objects,
                                                                mock_scrape_booking_site,
                                                                mock_send_email):
    """ Test when no object is found """
    # Simulate that getting all MonitoringRequest objects gets us the
    # mock_monitoring_request_object in the fixture
    mock_objects.all.return_value = []

    # Run the monitoring service
    monitoring_service()

    assert mock_scrape_booking_site.call_count == 0
    assert mock_send_email.call_count == 0
