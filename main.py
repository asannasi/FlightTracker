from emailer import send_debug_email
from flight import FlightTracker

flight = "DL-183"
ft = FlightTracker(flight)
print(ft)

sender_email = "me@gmail.com"
receiver_email = "you@gmail.com"
message = """\
    Subject: Hi
    There is a delay in your flight.
    """
isDelayed = ft.is_delayed_today()
print(isDelayed)
if (isDelayed == True):
    send_debug_email(sender_email, receiver_email, message)