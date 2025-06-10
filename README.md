# WEATHERLYYY_BOT

**Проект выполнен:**
Герасимова Мелания (ИСУ: 465525)
Яковлев Степан (ИСУ: 468173)

**📌 Описание проекта**

## WEATHERLYYY_BOT — Telegram-бот, который позволяет:

📍 Узнать текущую погоду по выбранному городу
💾 Сохранять города в избранное
📋 Просматривать список своих сохранённых мест
Бот использует API OpenWeatherMap и реализован с использованием aiogram, SQLAlchemy и FSM-механизма состояний.

## **⚙️ Функционал**

/weather — Показ текущей погоды по введённому городу (через OpenWeatherMap API)
/save_place — Сохранение города в избранное (через FSM + SQLite)
/my_places — Просмотр всех сохранённых городов
Дополнительно:

✅ Кэширование погоды (на 10 минут)
✅ Логирование событий в файл bot.log
✅ Inline/Reply-кнопки
✅ Админ-панель (рассылка, бан)
✅ Middleware и кастомные фильтры
✅ Мультиязычность (RU/EN)

## **🚀 Инструкция по запуску**

**Склонируйте репозиторий:**
git clone https://github.com/your_username/weatherlyyy_bot.git
cd weatherlyyy_bot

**Создайте и активируйте виртуальное окружение:**
python3 -m venv venv
source venv/bin/activate   # Для Linux/macOS
venv\Scripts\activate.bat  # Для Windows

**Установите зависимости:**
pip install -r requirements.txt

**Получите необходимые ключи:**
Telegram Bot Token:
Создайте бота через @BotFather в Telegram, следуя инструкциям.
Скопируйте токен, который он выдаст, — он нужен для переменной BOT_TOKEN.

OpenWeatherMap API Key:
Зарегистрируйтесь на https://openweathermap.org/ и создайте API-ключ в личном кабинете.
Он понадобится для переменной WEATHER_API_KEY.

**Настройте конфигурацию:**
Создайте файл .env и добавьте:
BOT_TOKEN=your_bot_token
WEATHER_API_KEY=your_openweathermap_api_key

**Запустите бота:**
python bot.py

**📂 Зависимости**
aiogram
SQLAlchemy
aiohttp
python-dotenv (если используется .env)
