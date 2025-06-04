import aiohttp
import time
from config.settings import settings

_weather_cache = {}

async def get_weather(city: str) -> str:
    city = city.lower()
    now = time.time()

    if city in _weather_cache and now - _weather_cache[city]["time"] < 600:
        return _weather_cache[city]["data"]

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.WEATHER_API_KEY}&units=metric"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                data = await response.json()
                result = f"Погода в {city.title()}: {data['weather'][0]['description']}, {data['main']['temp']}°C"
                _weather_cache[city] = {"data": result, "time": now}
                return result
    except Exception:
        return "Ошибка при запросе погоды."
