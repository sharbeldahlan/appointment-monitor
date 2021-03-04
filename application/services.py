from application.models import MonitoringRequest
from application.notification import send_email
from application.scraping import scrape_booking_site


def monitoring_service() -> None:
    """
    Main service that goes through the monitoring requests in the database.
    For each monitoring_request object, it:
        - calls scrape_booking_site() with the object's attributes
        - if the call returns available_appointment, it sends email to the object's to_email
    """
    # Get the instance of the monitoring request
    all_monitoring_requests = MonitoringRequest.objects.all()
    for monitoring_request in all_monitoring_requests:
        # Get the monitoring_request attributes: service_choice and office_choice
        service_choice = monitoring_request.service_choice
        # Get human-readable office choice of the monitoring_request, as the scraper would like
        office_choice = monitoring_request.get_office_choice_display()

        available_appointment = scrape_booking_site(service_choice=service_choice, office_choice=office_choice)
        if available_appointment:
            send_email(available_appointment=available_appointment, to_email=monitoring_request.to_email)
