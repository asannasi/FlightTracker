import smtplib
import ssl
import getpass

# sends an email to the debug server detailed in server.py
def send_debug_email(sender_email, receiver_email, message):
    client = smtplib.SMTP('localhost', port=1025)
    client.sendmail(sender_email, receiver_email, message)
    client.quit()

# sends an email to the specified gmail account
def send_gmail_email(sender_email, receiver_email, message):
    port = 465
    password = getpass.getpass()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
