import unittest
from weather_data import load_config, fetch_weather_data
from unittest.mock import patch

class TestWeatherData(unittest.TestCase):

    def test_load_config(self):
        config = load_config()
        self.assertIn('api_key', config)
        self.assertIsInstance(config['cities'], list)

    @patch('weather_data.requests.get')
    def test_fetch_weather_data(self, mock_get):
        # Simulate a successful API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'main': {
                'temp': 300,
                'feels_like': 298
            },
            'weather': [{'main': 'Clear'}]
        }
        
        config = load_config()
        city_weather = fetch_weather_data('Delhi', config['api_key'])
        self.assertIsInstance(city_weather, dict)
        self.assertIn('main', city_weather)
        self.assertEqual(city_weather['main']['temp'], 300)

if __name__ == '__main__':
    unittest.main()
