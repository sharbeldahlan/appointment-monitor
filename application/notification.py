import smtplib
from typing import Dict

from application.constants import FROM_EMAIL
from application.constants import FROM_PASSWORD


def send_email(available_appointment: Dict[str, str], to_email: str) -> None:
    """
    Main notification function, to send an email to the recipient
    with the appointment details.
    """
    # Extract the results
    date = available_appointment['date']
    available_time = available_appointment['available_time']

    # Setup SMTP server and login
    email_server = setup_smtp_server()

    # Create email
    # TODO message = ...

    # Send email and quit server
    # email_server.sendmail(FROM_EMAIL, to_email, message)
    email_server.quit()


def setup_smtp_server() -> smtplib.SMTP:
    """ Setup smtp and start connection """
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(FROM_EMAIL, FROM_PASSWORD)

    return server
