def monitoring_service():
    """
    Main service that goes through the monitoring requests in the database.
    For each monitoring_request object, it:
        - calls scrape_booking_site() with the object's attributes
        - if the call returns available_appointment, it sends email to the object's to_email
    """
    # Get the instance of the monitoring request.
        # Get the monitoring_request attributes: service_choice and office_choice
        # Get human-readable office choice of the monitoring_request, as the scraper would like.

        # available_appointment = scrape_booking_site()
        # if available_appointment:
        #    send_email()
