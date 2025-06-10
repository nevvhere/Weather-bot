from aiogram import types
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from storage.database import Session, BannedUser

class BanMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: types.Message, data: dict):
        session = Session()
        banned = session.query(BannedUser).filter_by(user_id=event.from_user.id).first()
        session.close()

        if banned:
            await event.answer("Вы заблокированы и не можете пользоваться ботом.")
            return

        return await handler(event, data)
