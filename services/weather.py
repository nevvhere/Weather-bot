import aiohttp
import asyncio
import time
from config.settings import settings

_weather_cache = {}

async def get_weather(city: str) -> str:
    city = city.lower()
    now = time.time()

    # Кэширование ответа на 10 минут
    if city in _weather_cache and now - _weather_cache[city]["time"] < 600:
        return _weather_cache[city]["data"]

    url = (
        f"http://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={settings.WEATHER_API_KEY}&units=metric"
    )

    try:
        timeout = aiohttp.ClientTimeout(total=10)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return "Сервис погоды временно недоступен."

                data = await response.json()
                result = (
                    f"Погода в {city.title()}: "
                    f"{data['weather'][0]['description']}, "
                    f"{data['main']['temp']}°C"
                )

                _weather_cache[city] = {"data": result, "time": now}
                return result

    except asyncio.TimeoutError:
        return "Превышено время ожидания ответа от сервера."
    except aiohttp.ClientError:
        return "Ошибка при подключении к сервису погоды."
    except Exception:
        return "Произошла непредвиденная ошибка при запросе погоды."
