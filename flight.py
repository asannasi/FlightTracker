import requests
import datetime
from lxml import html

class FlightTracker:
    def __init__(self, flight_number: str):
        self.flight = flight_number

    # Uses the flight number and date to form the flight url on kayak
    def generate_URL(self, date: datetime.datetime) -> str:
        url = "https://www.kayak.com/tracker/"
        date = str(d.year) + "-" + str(d.strftime('%m')) + "-" + str(d.strftime('%d'))
        url = url + self.flight + '/' + date
        return url

    # Uses the requests API to get the flight webpage as text
    def get_response(self, date: datetime.datetime) -> requests.Response:
        url = self.generate_URL(date)
        r = requests.get(url)
        return r
    
    # Parses the HTML text to find the tags with the relevant data
    def get_data_list(self, date: datetime.datetime) -> list:
        r = self.get_response(date)
        #turn the HTML response to bytes and then to a tree
        tree = html.fromstring(r.content) 
        # parse the tree using the hardcoded xpath expression
        data = tree.xpath('//div[@class="col-6-12"]/text()')
        return data

flight = "WN-203"
ft = FlightTracker(flight)
d = datetime.datetime.today()
col = ft.get_data_list(d)

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
