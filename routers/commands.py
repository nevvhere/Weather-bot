from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from services.weather import get_weather
from states.weather_states import WeatherStates
from storage.database import Session, UserPlace

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Я бот для погоды. Используй /help для списка команд.")

@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Доступные команды:\n"
        "/weather - Узнать погоду\n"
        "/save_place - Сохранить место\n"
        "/my_places - Мои места"
    )

@router.message(Command("weather"))
async def ask_city(message: Message, state: FSMContext):
    await message.answer("Введите город, чтобы узнать погоду:")
    await state.set_state(WeatherStates.waiting_for_weather_city)

@router.message(WeatherStates.waiting_for_weather_city)
async def show_weather(message: Message, state: FSMContext):
    weather = await get_weather(message.text)
    await message.answer(weather)
    await state.clear()

@router.message(Command("save_place"))
async def ask_place(message: Message, state: FSMContext):
    await message.answer("Введите название места для сохранения:")
    await state.set_state(WeatherStates.waiting_for_place)

@router.message(WeatherStates.waiting_for_place)
async def save_place(message: Message, state: FSMContext):
    session = Session()
    new_place = UserPlace(user_id=message.from_user.id, place_name=message.text)
    session.add(new_place)
    session.commit()
    session.close()

    await message.answer(f"Место '{message.text}' сохранено.")
    await state.clear()

@router.message(Command("my_places"))
async def my_places(message: Message):
    session = Session()
    places = session.query(UserPlace).filter_by(user_id=message.from_user.id).all()
    session.close()

    if not places:
        await message.answer("У вас нет сохранённых мест.")
    else:
        text = "\n".join([place.place_name for place in places])
        await message.answer(f"Ваши сохранённые места:\n{text}")
