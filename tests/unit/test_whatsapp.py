import sys
from types import ModuleType

import pytest

from stocknews import constants
from stocknews.domain.errors import ConfigError
from stocknews.infrastructure.whatsapp import WhatsAppNotifier, send_message


def test_send_message_calls_pywhatkit_when_installed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[tuple[str, str, int, bool]] = []
    fake = ModuleType("pywhatkit")

    def sendwhatmsg_instantly(
        phone: str, text: str, wait_time: int, tab_close: bool
    ) -> None:
        calls.append((phone, text, wait_time, tab_close))

    fake.sendwhatmsg_instantly = sendwhatmsg_instantly  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "pywhatkit", fake)
    WhatsAppNotifier("+4512345678").send_message("hello")
    assert calls == [("+4512345678", "hello", constants.SEND_WAIT_SECONDS, True)]


def test_send_message_raises_config_error_when_pywhatkit_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setitem(sys.modules, "pywhatkit", None)
    with pytest.raises(ConfigError, match="pywhatkit"):
        send_message("hello", "+45")
