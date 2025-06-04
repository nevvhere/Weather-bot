import logging
from aiogram import Bot, Dispatcher
from config.settings import settings
from routers.commands import router as commands_router

logging.basicConfig(
    level=logging.INFO,
    filename="bot.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()
dp.include_router(commands_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
