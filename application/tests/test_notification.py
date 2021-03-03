from unittest.mock import call
from unittest.mock import patch

from application.constants import BOOKING_SITE_URL
from application.constants import FROM_EMAIL
from application.notification import send_email
from application.notification import setup_smtp_server


@patch('application.notification.setup_smtp_server')
def test_send_email(mock_email_server):
    """ Test send_mail() with the SMTP server mocked. """
    available_appointment = {'available_time': '8:45', 'date': '26.02'}
    send_email(available_appointment=available_appointment, to_email="test@example.com")

    expected_message = f'Subject: Appointment Spotted!\n\n' \
                       f'Jee!\n\n' \
                       f'I spotted an appointment available on 26.02 at 8:45.\n\n' \
                       f'Book it now on {BOOKING_SITE_URL}.\n\n' \
                       f'Cheers,\n' \
                       f'Moni Tore'

    # We expect that there is one call to SMTP server's sendmail() with the following parameters
    expected_call = call().sendmail(FROM_EMAIL, 'test@example.com', expected_message)

    assert mock_email_server.call_count == 1
    assert expected_call in mock_email_server.mock_calls


def test_setup_smtp_server():
    """
    Test setup_smtp_server() by checking that it returns the correct type,
    so we know we set up an SMTP server correctly.
    """
    import smtplib
    server = setup_smtp_server()
    assert type(server) == smtplib.SMTP
    server.quit()
