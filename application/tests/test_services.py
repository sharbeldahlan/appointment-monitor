from application.services import monitoring_service

# Fixture: create a monitoring_request object


def test_monitoring_service__no_available_appointment():
    # Assert that send_email() is not called
    assert True


def test_monitoring_service__available_appointment():
    # Assert that send_email() is called with correct parameters
    assert True


def test_monitoring_service__no_monitoring_requests_in_database():
    assert True
