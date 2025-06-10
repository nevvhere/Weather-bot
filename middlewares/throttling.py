import asyncio
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message
from aiogram import types
from collections import defaultdict
import time

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, rate_limit: float = 1.0):
        self.rate_limit = rate_limit  # время между сообщениями
        self.user_timestamps = defaultdict(lambda: 0)

    async def __call__(self, handler, event: types.TelegramObject, data: dict):
        if isinstance(event, Message):
            user_id = event.from_user.id
            current_time = time.time()

            if current_time - self.user_timestamps[user_id] < self.rate_limit:
                await event.answer("Слишком часто. Подожди немного ⏳")
                return

            self.user_timestamps[user_id] = current_time

        return await handler(event, data)
