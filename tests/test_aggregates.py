import unittest
from aggregates import (
    average_temp,
    max_temp,
    min_temp,
    dominant_weather
)

class TestAggregates(unittest.TestCase):

    def test_calculate_average_temperature(self):
        # Normal case
        temperatures = [30.5, 32.0, 28.0, 35.5]
        average = average_temp(temperatures)
        self.assertAlmostEqual(average, 31.0)

        # Edge case: empty list
        average_empty = average_temp([])
        self.assertEqual(average_empty, 0)

        # Edge case: single temperature
        average_single = average_temp([25.0])
        self.assertEqual(average_single, 25.0)

    def test_find_maximum_temperature(self):
        temperatures = [30.5, 32.0, 28.0, 35.5]
        maximum = max_temp(temperatures)
        self.assertEqual(maximum, 35.5)

        # Edge case: empty list
        maximum_empty = max_temp([])
        self.assertIsNone(maximum_empty)

    def test_find_minimum_temperature(self):
        temperatures = [30.5, 32.0, 28.0, 35.5]
        minimum = min_temp(temperatures)
        self.assertEqual(minimum, 28.0)

        # Edge case: empty list
        minimum_empty = min_temp([])
        self.assertIsNone(minimum_empty)

    def test_get_dominant_weather_condition(self):
        weather_conditions = ['Clear', 'Rain', 'Clear', 'Cloudy', 'Clear']
        dominant = dominant_weather(weather_conditions)
        self.assertEqual(dominant, 'Clear')

        # Edge case: empty list
        dominant_empty = dominant_weather([])
        self.assertIsNone(dominant_empty)

if __name__ == '__main__':
    unittest.main()
