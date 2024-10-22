

def check_alerts(weather_data, threshold):
    """Check if any alerts should be triggered based on weather data."""
    if weather_data:
        current_temp = weather_data['main']['temp']
        if current_temp > threshold:
            print(f"Alert! Current temperature is {current_temp}°C, which exceeds the threshold of {threshold}°C.")
