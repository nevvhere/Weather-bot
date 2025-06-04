import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

settings = Settings()
