import requests
import datetime
from lxml import html

class FlightTracker:
    def __init__(self, flight_number: str):
        self.flight = flight_number

    # Uses the flight number and date to form the flight url on kayak
    def generate_URL(self, date: datetime.datetime) -> str:
        url = "https://www.kayak.com/tracker/"
        date = str(date.year) + "-" + str(date.strftime('%m')) + "-" + str(date.strftime('%d'))
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

    # From the data parsed by the HTML text, get the scheduled and
    # estimated arrival times. This is kind of a hardcoded index because
    # it looks for the label in the list and then takes the list item 
    # after it. This assumes data is listed with field and then value.
    # Returns a list of scheduled arrival time and estimated arrival time.
    def get_text_times(self, data: list) -> list:
        print(data)
        scheduled_time = ""
        estimated_time = ""
        for i in range(0, len(data)):
            if data[i] == "Scheduled Arrival":
                scheduled_time = data[i+1]
            elif data[i] == "Estimated Arrival":
                estimated_time = data[i+1]
        return [scheduled_time, estimated_time]

    def text_times_to_24_datetimes(self, text_times: list) -> list:
        converted_times = []
        for time in text_times:
            time_list = time.split(" ")
            # time list should be in format like ['10:39', 'am', 'PST']
            assert(len(time_list) == 3)
            # change time from string to ints for hour and minutes
            int_time = time_list[0].split(":")
            int_time = [int(t) for t in int_time]
            if time_list[1] == "pm":
                int_time[0] += 12
            d = datetime.datetime.today() #dummy values...needs to be changed to handle flights spanning two days
            dt = datetime.datetime(d.year, d.month, d.day, int_time[0], int_time[1])
            converted_times.append(dt)
        return converted_times

    def is_delayed_today(self) -> bool:
        d = datetime.datetime.today()
        data = ft.get_data_list(d)
        text_times = ft.get_text_times(data)
        times = ft.text_times_to_24_datetimes(text_times)
        scheduled_time = times[0]
        estimated_time = times[1]
        return scheduled_time.time() < estimated_time.time()

flight = "DL-183"
ft = FlightTracker(flight)
print(ft.is_delayed_today())