import smtplib
import ssl
#import getpass

def send_debug_email(sender_email, receiver_email, message):
    client = smtplib.SMTP('localhost', port=1025)
    client.sendmail(sender_email, receiver_email, message)
    client.quit()

#for gmail
'''
password = getpass.getpass()
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.localhost", port, context=context) as server:
    #server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
'''