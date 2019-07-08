import smtplib
import ssl
import getpass

port = 1025
sender_email = "me@gmail.com"
password = getpass.getpass()
receiver_email = "you@gmail.com"

context = ssl.create_default_context()

with smtplib.SMTP_SSL("localhost", port, context=context) as server:
    #server.login(sender_email, password)
    message = """\
        Subject: Hi
        There is a delay in your flight.
        """
    server.sendmail(sender_email, receiver_email, message)
