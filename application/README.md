# Application Technical Walkthrough

## Entry point
The appointment monitor application's entry point is the `views.py`.

That is where the main view, `MonitoringRequestView` is, and the first thing reached when the server is requested.

`MonitoringRequestView` contains `MonitoringRequestForm`, which exposes the `MonitoringRequest` fields.

`MonitoringRequest` is our database object that contains the details of the monitoring request:

- `service_choice`: Appointment service type chosen by the user.
- `office_choice`: Migri office location chosen for the Appointment.
- `to_email`: Email address to which an email with the available appointment details is sent.

The `service_choice` and `office_choice` are defined in `constants.py`.

Once a `MonitoringRequest` object is instantiated, the main task of `services.py` will run periodically to check all
the monitoring_request instances and monitor appointments based on their attributes.

## Main service of the monitoring
The `monitoring_service()` function in `services.py` will use the logic in `scraping.py` and `notification.py` to do the scraping 
and notification. For each `MonitoringRequest` object in the database, it will do the following:
1. Call `scrape_booking_site()` with the object's attributes.
1. If the first call returns result, call `send_email()` with the details of the result.

## Tests
Tests are found in `application.tests` package. Each module described above (`views.py`, `services.py`, `scraping.py`,
and `notification.py`) has a corresponding test module in the
`tests` package. Additionally, there is a `test_integration.py` where end-to-end tests should go.
