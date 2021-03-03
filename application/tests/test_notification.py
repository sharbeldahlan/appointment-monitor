from application.notification import setup_smtp_server


def test_setup_smtp_server():
    """
    Test setup_smtp_server() by checking that it returns the correct type,
    so we know we set up an SMTP server correctly.
    """
    import smtplib
    server = setup_smtp_server()
    assert type(server) == smtplib.SMTP
    server.quit()
