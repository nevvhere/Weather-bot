from aiogram.fsm.state import State, StatesGroup

class WeatherStates(StatesGroup):
    waiting_for_place = State()
    waiting_for_weather_city = State()
