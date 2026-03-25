import asyncio
from unittest.mock import MagicMock

import pytest
from aiogram.types import User

from src.config import Config, TgBot
from src.filters.user import UserFilter


@pytest.fixture
def sample_config() -> Config:
    return Config(tg_bot=TgBot(token="t", admin_ids=[1, 2]))


def test_user_filter_allows_non_admin(sample_config: Config):
    async def run() -> bool:
        f = UserFilter()
        msg = MagicMock()
        user = User(id=99, is_bot=False, first_name="u")
        return await f.__call__(msg, user, sample_config)

    assert asyncio.run(run()) is True


def test_user_filter_blocks_admin(sample_config: Config):
    async def run() -> bool:
        f = UserFilter()
        msg = MagicMock()
        user = User(id=1, is_bot=False, first_name="u")
        return await f.__call__(msg, user, sample_config)

    assert asyncio.run(run()) is False
