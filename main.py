import requests
import pprint


class WeatherRequest:
    def __init__(self, latitude, longitude, date, parameters):
        self.latitude = latitude
        self.longitude = longitude
        self.date = date
        self.parameters = parameters

    def make_request(self):
        parameters_str = ','.join(self.parameters)
        url = (f"https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.longitude}"
               f"&hourly={parameters_str}&start={self.date}T00:00:00Z&end={self.date}T23:59:59Z")
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Error:{response.status_code}')
            return None


latitude = 47.23571
longitude = 39.70151
date = '2024-07-11'
parameters = ['temperature_2m', 'precipitation', 'windspeed_10m']

obj = WeatherRequest(latitude, longitude, date, parameters)
ans = obj.make_request()
pprint.pprint(ans)
print()
print(ans['hourly']['temperature_2m'])
print(ans['hourly']['time'])
