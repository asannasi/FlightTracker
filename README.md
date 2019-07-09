# FlightTracker
The goal of this program is to send automatic emails when it detects a flight is delayed.

Written in python3.

Solves the problem of having to give your email to a company to get alerts. 

Flight data is taken from https://www.kayak.com/tracker/ since the website provides data in the HTML returned after a request instead of in a variable which at this point I'm unsure how to access the value of. I am using the Requests API with python to send HTTP requests to the flight tracker website and then looking through the text returned to find the estimated arrival time and the scheduled arrival time.

Basic functionality:
 - Get accurate flight data through HTML requests
 - Parse the result to get the flight data, including the estimated arrival time and the scheduled arrival time
 - Check if the flight is delayed
 - If the flight is delayed, then send an email with how long the delay is

Robust functionality:
 - Make sure the times can be compared with AM and PM
 - Only one email should be sent for some delay threshold
 - raise error if flight not found

Extra functionality (not implemented):
 - If the program starts before midnight and ends after midnight, it should still work
 - Handle the case of arrival times spaced out before midnight and after midnight (I'm not sure how the kayak website handles this and there is no easy way to find a test case)

Citations:
https://2.python-requests.org/en/master/user/quickstart/
https://www.w3schools.com/tags/ref_httpmethods.asp
https://www.kayak.com/tracker/WN-203/2019-07-07
https://docs.python-guide.org/scenarios/scrape/
https://realpython.com/python-send-email/
and some stackoverflow posts
