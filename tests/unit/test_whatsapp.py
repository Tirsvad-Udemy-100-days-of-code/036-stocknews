import sys
from types import ModuleType

import pytest

from stocknews import constants
from stocknews.domain.errors import NotificationError
from stocknews.infrastructure.whatsapp import WhatsAppNotifier, send_message


def test_send_message_calls_pywhatkit_when_installed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[tuple[str, str, int, bool, int]] = []
    fake = ModuleType("pywhatkit")

    def sendwhatmsg_instantly(
        phone_no: str, message: str, wait_time: int, tab_close: bool, close_time: int
    ) -> None:
        calls.append((phone_no, message, wait_time, tab_close, close_time))

    fake.sendwhatmsg_instantly = sendwhatmsg_instantly  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "pywhatkit", fake)
    WhatsAppNotifier("+4512345678").send_message("hello")
    assert calls == [
        (
            "+4512345678",
            "hello",
            constants.WHATSAPP_WEB_WAIT_SECONDS,
            True,
            constants.WHATSAPP_WEB_CLOSE_SECONDS,
        )
    ]


def test_send_message_raises_notification_error_when_pywhatkit_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setitem(sys.modules, "pywhatkit", None)
    with pytest.raises(NotificationError, match=r"pip install -e \.\[whatsapp\]"):
        send_message("hello", "+45")


def test_notifier_sends_stripped_phone_through_injected_send() -> None:
    sent: list[tuple[str, str]] = []
    notifier = WhatsAppNotifier(" +4512345678 ", send=lambda t, p: sent.append((t, p)))
    notifier.send_message("hi")
    assert sent == [("hi", "+4512345678")]


def test_notifier_rejects_number_without_plus() -> None:
    notifier = WhatsAppNotifier("4512345678", send=lambda t, p: None)
    with pytest.raises(NotificationError, match=constants.ENV_PHONE_NUMBER):
        notifier.send_message("hi")


def test_notifier_wraps_send_failure_without_the_number() -> None:
    def failing(text: str, phone: str) -> None:
        raise RuntimeError(f"boom {phone}")

    notifier = WhatsAppNotifier("+4512345678", send=failing)
    with pytest.raises(NotificationError, match="logged in") as info:
        notifier.send_message("hi")
    assert "4512345678" not in str(info.value)
    assert isinstance(info.value.__cause__, RuntimeError)


def test_notifier_passes_notification_error_through() -> None:
    def failing(text: str, phone: str) -> None:
        raise NotificationError("not installed")

    notifier = WhatsAppNotifier("+45", send=failing)
    with pytest.raises(NotificationError, match="not installed"):
        notifier.send_message("hi")
