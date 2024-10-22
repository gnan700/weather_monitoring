from flask import Flask, render_template, jsonify
import time
from threading import Thread
from weather_data import fetch_weather_data, load_config
from alerts import check_alerts
from aggregates import update_daily_summary

app = Flask(__name__)

weather_data_cache = []  # Store the latest weather data

def fetch_and_process_weather():
    config = load_config()
    api_key = config['api_key']
    cities = config['cities']
    interval = config['interval']
    temperature_threshold = config['temperature_threshold']

    while True:
        for city in cities:
            weather_data = fetch_weather_data(city, api_key)
            if weather_data:
                update_daily_summary(city, weather_data)
                alert = check_alerts(weather_data, temperature_threshold)
                weather_data_cache.append({
                    'city': city,
                    'temp': weather_data['main']['temp'],
                    'condition': weather_data['weather'][0]['description'],
                    'alert': alert
                })

        # Wait for the configured interval before the next fetch
        time.sleep(interval)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def weather():
    return jsonify(weather_data_cache)

def main():
    # Start the weather data fetching in a separate thread
    weather_thread = Thread(target=fetch_and_process_weather)
    weather_thread.start()

    # Start the Flask app
    app.run(debug=True, use_reloader=False, port=5001)  # Set use_reloader=False to avoid threading issues

if __name__ == "__main__":
    main()
