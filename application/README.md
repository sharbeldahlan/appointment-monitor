# Application Technical Walkthrough

## View
The appointment monitor application's entry point is the `views.py`.

That is where the main view, `MonitoringRequestCreate`, is, and the first thing reached when the server is requested.

`MonitoringRequestCreate` inherits from Django's class-based `CreateView`, which enables creation of instances of
models in our project. The view exposes fields of the `MonitoringRequest` model.

## Model
The `MonitoringRequest` model is a representation of our database table that contains the details of the
monitoring request:

- `service_choice`: Appointment service type chosen by the user.
- `office_choice`: Migri office location chosen for the Appointment.
- `to_email`: Email address to which an email with the available appointment details is sent.

The different choices that `service_choice` and `office_choice` fields have are defined in `constants.py`.

Multiple `MonitoringRequest` objects can be instantiated and stored in the database. 

The main task of `services.py` runs periodically to check all the monitoring request instances and monitor
appointments based on each instance's attributes.

## Main service of the monitoring
The `monitoring_service()` function in `services.py` will use the logic in `scraping.py` and `notification.py` to do the scraping 
and notification. For each `MonitoringRequest` object in the database, it will do the following:
1. Call `scrape_booking_site()` with the object's attributes.
1. If the first call returns result, call `send_email()` with the details of the result.

Every 10 minutes, the `monitoring_service()` is run by a cron job. Cron jobs can be found in a list called `CRONJOBS`,
which is defined inside `project/settings.py`.

## Tests
Tests are found in `application.tests` package. Each module described above (`views.py`, `services.py`, `scraping.py`,
and `notification.py`) has a corresponding test module in the
`tests` package. Additionally, there is a `test_integration.py` where end-to-end tests are.
