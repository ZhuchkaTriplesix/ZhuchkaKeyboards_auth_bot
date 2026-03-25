"""Tests for config loading."""

from __future__ import annotations

from pathlib import Path

import pytest

from src.config import load_config


def test_load_config_parses_token_and_admin_ids(tmp_path: Path) -> None:
    p = tmp_path / "config.ini"
    p.write_text(
        "[bot]\ntoken = test_token\nadmin_ids = 10, 20, 30\n",
        encoding="utf-8",
    )
    cfg = load_config(p)
    assert cfg.tg_bot.token == "test_token"
    assert cfg.tg_bot.admin_ids == [10, 20, 30]


def test_load_config_empty_admin_ids(tmp_path: Path) -> None:
    p = tmp_path / "config.ini"
    p.write_text("[bot]\ntoken = x\n", encoding="utf-8")
    cfg = load_config(p)
    assert cfg.tg_bot.admin_ids == []


def test_load_config_missing_file_raises() -> None:
    with pytest.raises(FileNotFoundError):
        load_config(Path("/nonexistent/bot.ini"))


def test_load_config_token_from_env_overrides_ini(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "from_env")
    monkeypatch.delenv("BOT_TOKEN", raising=False)
    p = tmp_path / "config.ini"
    p.write_text("[bot]\ntoken = from_ini\nadmin_ids = 1\n", encoding="utf-8")
    cfg = load_config(p)
    assert cfg.tg_bot.token == "from_env"
    assert cfg.tg_bot.admin_ids == [1]
