import logging
from aiogram import Bot, Dispatcher
from config.settings import settings
from routers.commands import router as commands_router
from middlewares.throttling import ThrottlingMiddleware
from routers import admin_panel
from middlewares.ban import BanMiddleware


logging.basicConfig(
    level=logging.INFO,
    filename="bot.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()
dp.include_router(commands_router)
dp.message.outer_middleware(ThrottlingMiddleware(rate_limit=1.5))
dp.include_router(admin_panel.router)
dp.message.outer_middleware(BanMiddleware())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
