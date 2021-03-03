import smtplib

from application.constants import FROM_EMAIL
from application.constants import FROM_PASSWORD


def setup_smtp_server() -> smtplib.SMTP:
    """ Setup smtp and start connection """
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(FROM_EMAIL, FROM_PASSWORD)

    return server
