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
 - If the program starts before midnight and ends after midnight, it should still work
 - Putting an invalid date outside kayak's thresholds should result in an error
 - if a flight is not found, should check other dates and notify user

Extra functionality:
 - undecided

Still working on robust functionality

Citations:
https://2.python-requests.org/en/master/user/quickstart/
https://www.w3schools.com/tags/ref_httpmethods.asp
https://www.kayak.com/tracker/WN-203/2019-07-07
view-source:https://www.kayak.com/tracker/WN-203/2019-07-07
https://docs.python-guide.org/scenarios/scrape/
https://stackoverflow.com/questions/1831410/python-time-comparison

https://realpython.com/python-send-email/#option-2-setting-up-a-local-smtp-server
