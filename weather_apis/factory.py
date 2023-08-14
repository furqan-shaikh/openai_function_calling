
from weather_apis.dummy_api import get_current_weather


def get_current_weather_from_provider(weather_provider: str):
    if weather_provider == "dummy":
        return get_current_weather
