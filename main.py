from emailer import send_debug_email
from flight import FlightTracker

flight = "DL-181092"
ft = FlightTracker(flight)
#sends delayed email every 30 minutes or if something changes
delay_time = 0
while True:
    sender_email = "me@gmail.com"
    receiver_email = "you@gmail.com"
    message = """\
        Subject: Hi
        There is a delay in your flight.
        """
    delay = ft.is_delayed_today()
    if delay != delay_time:
        delay_time = delay
        send_debug_email(sender_email, receiver_email, message)