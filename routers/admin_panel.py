from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from filters.admin_filter import AdminFilter
from states.admin_states import AdminStates
from storage.database import Session, BannedUser

router = Router()

ADMIN_IDS = [1290806755]

# Команда /broadcast
@router.message(AdminFilter(admin_ids=ADMIN_IDS), Command("broadcast"))
async def start_broadcast(message: Message, state: FSMContext):
    await message.answer("Введите текст для рассылки:")
    await state.set_state(AdminStates.waiting_for_broadcast_text)

@router.message(AdminStates.waiting_for_broadcast_text)
async def process_broadcast(message: Message, state: FSMContext):
    from aiogram import Bot
    from storage.database import Session, UserPlace

    broadcast_text = message.text
    session = Session()

    user_ids = session.query(UserPlace.user_id).distinct().all()
    banned_ids = session.query(BannedUser.user_id).all()
    banned_set = {b[0] for b in banned_ids}

    bot: Bot = message.bot
    count = 0

    for (user_id,) in user_ids:
        if user_id in banned_set:
            continue
        try:
            await bot.send_message(user_id, broadcast_text)
            count += 1
        except:
            continue

    await message.answer(f"Сообщение отправлено {count} пользователям.")
    await state.clear()

# Команда /ban
@router.message(AdminFilter(admin_ids=ADMIN_IDS), Command("ban"))
async def start_ban(message: Message, state: FSMContext):
    await message.answer("Введите ID пользователя, которого нужно забанить:")
    await state.set_state(AdminStates.waiting_for_ban_id)

@router.message(AdminStates.waiting_for_ban_id)
async def process_ban(message: Message, state: FSMContext):
    session = Session()
    try:
        user_id = int(message.text)
        banned = BannedUser(user_id=user_id)
        session.add(banned)
        session.commit()
        await message.answer(f"Пользователь {user_id} заблокирован.")
    except:
        await message.answer("Ошибка: введите корректный ID.")
    finally:
        session.close()
        await state.clear()
