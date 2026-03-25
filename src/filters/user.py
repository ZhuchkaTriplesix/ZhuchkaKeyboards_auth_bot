from aiogram.filters import BaseFilter
from aiogram.types import Message, User

from src.config import Config


class UserFilter(BaseFilter):
    """Passes for users whose id is not in ``config.tg_bot.admin_ids``."""

    async def __call__(self, _message: Message, event_from_user: User, config: Config) -> bool:
        return event_from_user.id not in config.tg_bot.admin_ids
