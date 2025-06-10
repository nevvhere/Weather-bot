from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from services.weather import get_weather
from states.weather_states import WeatherStates
from storage.database import Session, UserPlace
from keyboards.reply import main_reply_keyboard, confirm_save_keyboard
from filters.admin_filter import AdminFilter
from filters.keyword_filter import KeywordFilter

router = Router()


# /start — приветствие и главное меню
@router.message(Command("start"))
async def cmd_start(message: Message):
    session = Session()
    exists = session.query(UserPlace).filter_by(user_id=message.from_user.id).first()
    if not exists:
        dummy = UserPlace(user_id=message.from_user.id, place_name="-")
        session.add(dummy)
        session.commit()
    session.close()

    await message.answer(
        "Привет! Я — твой погодный бот.\nВыбери действие:",
        reply_markup=main_reply_keyboard
    )


# /help — список команд
@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Доступные команды:\n"
        "/weather - Узнать погоду\n"
        "/my_places - Мои места"
    )


# Узнать погоду — ввод города
@router.message(Command("weather"))
@router.message(F.text == "Узнать погоду")
async def ask_city(message: Message, state: FSMContext):
    await message.answer("Введите город, чтобы узнать погоду:")
    await state.set_state(WeatherStates.waiting_for_weather_city)


# Показать погоду и предложить сохранить
@router.message(WeatherStates.waiting_for_weather_city)
async def show_weather(message: Message, state: FSMContext):
    weather = await get_weather(message.text)
    await message.answer(weather)

    await message.answer(
        "Хочешь сохранить этот город?",
        reply_markup=confirm_save_keyboard
    )

    await state.update_data(city=message.text)
    await state.set_state(WeatherStates.waiting_for_place)


# Сохранить место
@router.message(F.text == "Сохранить место")
async def save_place(message: Message, state: FSMContext):
    data = await state.get_data()
    city = data.get("city")

    if not city:
        await message.answer("Сначала узнай погоду, чтобы сохранить место.")
        return

    session = Session()
    new_place = UserPlace(user_id=message.from_user.id, place_name=city)
    session.add(new_place)
    session.commit()
    session.close()

    await message.answer(
        f"Город '{city}' сохранён.",
        reply_markup=main_reply_keyboard
    )
    await state.clear()


# Не сохранять место
@router.message(F.text == "Не сохранять")
async def cancel_save(message: Message, state: FSMContext):
    await message.answer("Город не сохранён.", reply_markup=main_reply_keyboard)
    await state.clear()


# Мои места
@router.message(Command("my_places"))
@router.message(F.text == "Мои места")
async def my_places(message: Message):
    session = Session()
    places = session.query(UserPlace).filter_by(user_id=message.from_user.id).all()
    session.close()

    if not places:
        await message.answer("У вас нет сохранённых мест.")
    else:
        text = "\n".join([place.place_name for place in places])
        await message.answer(f"Ваши сохранённые места:\n{text}")


# Фильтр: ты админ?
@router.message(AdminFilter(admin_ids=[1290806755]), Command("admin"))
async def admin_only(message: Message):
    await message.answer("Ты админ, привет!")


# Фильтр: ключевое слово "погода"
@router.message(KeywordFilter(keyword="погода"))
async def keyword_detected(message: Message):
    await message.answer("Ты упомянул погоду!")
