import datetime
#from requests_html import HTMLSession
import requests
from lxml import html
'''
url = "https://flightaware.com/live/flight/"
flight = "SWA203"
'''
url = "https://www.kayak.com/tracker/"
flight = "WN-203"
d = datetime.datetime.today()
date = str(d.year) + "-" + str(d.strftime('%m')) + "-" + str(d.strftime('%d'))
url = url + flight + '/' + date
'''
session = HTMLSession()
r = session.get(url)
'''
r = requests.get(url)
text = r.text
tree = html.fromstring(r.content)
col = tree.xpath('//div[@class="col-6-12"]/text()')
print(col)

scheduled_time = ""
estimated_time = ""
for i in range(0, len(col)):
    if col[i] == "Scheduled Arrival":
        scheduled_time = col[i+1]
    elif col[i] == "Estimated Arrival":
        estimated_time = col[i+1]

scheduled_time = scheduled_time.split(" ")[0].split(":")
estimated_time = estimated_time.split(" ")[0].split(":")

scheduled_time = datetime.datetime(d.year, d.month, d.day, int(scheduled_time[0]), int(scheduled_time[1]))
estimated_time = datetime.datetime(d.year, d.month, d.day, int(estimated_time[0]), int(estimated_time[1]))

print("Scheduled Time: ", scheduled_time)
print("Estimated Time:", estimated_time)
if scheduled_time.time() < estimated_time.time():
    print("Delayed")
else:
    print("On Time")