from flask import Flask, jsonify, request, render_template, send_from_directory
import requests

app = Flask(__name__)


def get_weather_data(latitude: float, longitude: float, date: str, parameters: list):
    parameters_str = ','.join(parameters)
    url = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
           f"&hourly={parameters_str}&start={date}T00:00:00Z&end={date}T23:59:59Z")

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': f'API request failed with status {response.status_code}'}


@app.route('/weather', methods=['GET'])
def weather():
    latitude = request.args.get('latitude', type=float)
    longitude = request.args.get('longitude', type=float)
    date = request.args.get('date', type=str)
    parameters = request.args.getlist('parameters')

    if not latitude or not longitude or not date or not parameters:
        return jsonify({'Error': 'Not enough required parameters'}), 400

    response = get_weather_data(latitude, longitude, date, parameters)

    images = ['sun.png' if precipitation == 0 else 'cloud.png' if precipitation < 0.4 else 'storm.png' for precipitation
              in
              response['hourly']['precipitation']]
    if 'error' in response:
        return jsonify(response), 500
    else:
        return render_template('table.html', time=response['hourly']['time'],
                               precipitation=response['hourly']['precipitation'],
                               windspeed=response['hourly']['windspeed_10m'],
                               temperature=response['hourly']['temperature_2m'],
                               length=len(response['hourly']['time']), image_name=images), 200


@app.route('/table')
def table():
    data = [
        {"date": "10.01.2010", "temperature": 30, "city": "Moscow"},
        {"date": "10.01.2010", "temperature": 30, "city": "SPB"},
        {"date": "10.01.2010", "temperature": 30, "city": "Rostov"},
    ]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
