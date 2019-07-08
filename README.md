# FlightTracker
The goal of this program is to send automatic emails when it detects a flight is delayed.

Flight data is taken from https://www.kayak.com/tracker/ since the website provides data in the HTML returned after a request instead of in a variable which at this point I'm unsure how to access the value of. I am using the Requests API with python to send HTTP requests to the flight tracker website and then looking through the text returned to find the estimated arrival time and the scheduled arrival time.

Basic functionality:
 - Get accurate flight data through HTML requests
 - Parse the result to get the flight data, including the estimated arrival time and the scheduled arrival time
 - Check if the flight is delayed
 - If the flight is delayed, then send an email with how long the delay is

Robust functionality:
 - Make sure the times can be compared with AM and PM
 - Only one email should be sent for some delay threshold

Extra functionality:
 - 

At this time, I am trying to get basic functionality working.