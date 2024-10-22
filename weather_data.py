
import requests
import yaml

def load_config():
    """Load configuration from YAML file."""
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config

def fetch_weather_data(city, api_key):
    """Fetch weather data for a specified city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Return the weather data as JSON
    else:
        print(f"Failed to fetch data for {city}. Error: {response.status_code} - {response.text}")
        return None
