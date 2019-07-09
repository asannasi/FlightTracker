import smtpd
import asyncore

#starts a local debug server
server = smtpd.SMTPServer(('localhost', 1025), None)
asyncore.loop()

#or use "python -m smtpd -n -c DebuggingServer localhost:1025" in command line