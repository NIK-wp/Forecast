import requests


def WeatherRequest(latitude: float, longitude: float, date: str, parameters: [str]):
    parameters_str = ','.join(parameters)
    url = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
           f"&hourly={parameters_str}&start={date}T00:00:00Z&end={date}T23:59:59Z")
    response = requests.get(url)
    if response.status_code == 200:
        ans = response.json()
        print(date)
        for i in range(len(ans['hourly']['temperature_2m'])):
            print(
                f"{ans['hourly']['time'][i][-5:]}: температура - {ans['hourly']['temperature_2m'][i]}°C, "
                f"осадки - {ans['hourly']['precipitation'][i]}mm,"
                f" ветер -  {ans['hourly']['windspeed_10m'][i]}km/h")
    else:
        print(f'Error:{response.status_code}')
        return None


latitude_test = 47.23571
longitude_test = 39.70151
date_test = '2024-07-11'
parameters_test = ['temperature_2m', 'precipitation', 'windspeed_10m']
WeatherRequest(latitude_test, longitude_test, date_test, parameters_test)
