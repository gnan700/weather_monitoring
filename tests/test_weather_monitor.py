import unittest
from app import app
from weather_data import fetch_weather_data

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Weather Monitoring System', response.data)

    def test_fetch_weather_data(self):
        # Test the fetch_weather_data function for a known city
        api_key = 'your_openweathermap_api_key'
        data = fetch_weather_data('Delhi', api_key)
        self.assertIn('temp', data)
        self.assertIn('feels_like', data)

if __name__ == '__main__':
    unittest.main()
