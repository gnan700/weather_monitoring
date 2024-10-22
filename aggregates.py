from datetime import datetime
from collections import defaultdict

daily_summaries = defaultdict(lambda: {'temp_sum': 0, 'count': 0, 'max_temp': float('-inf'), 'min_temp': float('inf'), 'weather_conditions': defaultdict(int)})

def update_daily_summary(city, weather_data):
    """Update the daily summary with the latest weather data."""
    if weather_data:
        date = datetime.fromtimestamp(weather_data['dt']).date()
        daily_summaries[date]['temp_sum'] += weather_data['main']['temp']
        daily_summaries[date]['count'] += 1
        daily_summaries[date]['max_temp'] = max(daily_summaries[date]['max_temp'], weather_data['main']['temp'])
        daily_summaries[date]['min_temp'] = min(daily_summaries[date]['min_temp'], weather_data['main']['temp'])
        dominant_condition = weather_data['weather'][0]['main']
        daily_summaries[date]['weather_conditions'][dominant_condition] += 1

def calculate_daily_aggregates(date):
    """Calculate daily aggregates."""
    if date in daily_summaries:
        summary = daily_summaries[date]
        average_temp = summary['temp_sum'] / summary['count']
        dominant_weather = max(summary['weather_conditions'], key=summary['weather_conditions'].get)
        return {
            'date': date,
            'average_temp': average_temp,
            'max_temp': summary['max_temp'],
            'min_temp': summary['min_temp'],
            'dominant_weather': dominant_weather
        }
    return None
