# WEATHERLYYY_BOT

**Проект выполнен:**  
Герасимова Мелания (ИСУ: 465525)  
Яковлев Степан (ИСУ: 468173)

---

## 📌 Описание проекта

**WEATHERLYYY_BOT** — Telegram-бот, который позволяет:

- 📍 Узнать текущую погоду по выбранному городу  
- 💾 Сохранять города в избранное  
- 📋 Просматривать список своих сохранённых мест

Бот использует API OpenWeatherMap и реализован с использованием `aiogram`, `SQLAlchemy` и FSM-механизма состояний.

---

## ⚙️ Функционал

- `/weather` — Показ текущей погоды по введённому городу (через OpenWeatherMap API)  
- `/save_place` — Сохранение города в избранное (через FSM + SQLite)  
- `/my_places` — Просмотр всех сохранённых городов  

**Дополнительно:**

- ✅ Кэширование погоды (на 10 минут)  
- ✅ Логирование событий в файл `bot.log`  
- ✅ Inline/Reply-кнопки  
- ✅ Админ-панель (рассылка, бан)  
- ✅ Middleware и кастомные фильтры  
- ✅ Мультиязычность (RU/EN)

---

## 🚀 Инструкция по запуску

1. **Склонируйте репозиторий:**
   ```bash
   git clone https://github.com/your_username/weatherlyyy_bot.git
   cd weatherlyyy_bot
   ```

2. **Создайте и активируйте виртуальное окружение:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Для Linux/macOS
   venv\Scripts\activate.bat  # Для Windows
   ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Получите необходимые ключи:**

   - **Telegram Bot Token:**  
     Создайте бота через [@BotFather](https://t.me/BotFather) в Telegram и получите токен (`BOT_TOKEN`).

   - **OpenWeatherMap API Key:**  
     Зарегистрируйтесь на [https://openweathermap.org/](https://openweathermap.org/), получите API-ключ (`WEATHER_API_KEY`).

5. **Настройте конфигурацию:**  
   Создайте файл `.env` и добавьте:

   ```env
   BOT_TOKEN=your_bot_token
   WEATHER_API_KEY=your_openweathermap_api_key
   ```

6. **Запустите бота:**
   ```bash
   python bot.py
   ```

---

## 📂 Зависимости

- aiogram  
- SQLAlchemy  
- aiohttp  
- python-dotenv 
