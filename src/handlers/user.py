from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("me"))
async def cmd_me(message: Message):
    """
    Handler for /me command. Returns user information.
    Available for all users.
    """
    user = message.from_user

    if not user:
        await message.answer("❌ Не удалось получить информацию о пользователе.")
        return

    user_info = f"👤 <b>Информация о пользователе</b>\n\n🆔 <b>ID:</b> <code>{user.id}</code>\n"

    if user.username:
        user_info += f"📝 <b>Username:</b> @{user.username}\n"

    if user.first_name:
        user_info += f"👋 <b>Имя:</b> {user.first_name}\n"

    if user.last_name:
        user_info += f"👋 <b>Фамилия:</b> {user.last_name}\n"

    if user.language_code:
        user_info += f"🌐 <b>Язык:</b> {user.language_code}\n"

    user_info += f"🤖 <b>Бот:</b> {'Да' if user.is_bot else 'Нет'}\n"

    if user.is_premium:
        user_info += "⭐ <b>Premium:</b> Да\n"

    await message.answer(user_info)


def register_user(dp_or_router):
    dp_or_router.include_router(router)
