"""WhatsApp sender built on pywhatkit, an optional dependency."""

import importlib

from stocknews import constants
from stocknews.domain.errors import ConfigError


def send_message(text: str, phone: str) -> None:
    """Send a message to a phone number with WhatsApp Web.

    @param text The message.
    @param phone The recipient in international format, like +4512345678.
    @throws ConfigError when pywhatkit is not installed.
    """
    try:
        pywhatkit = importlib.import_module("pywhatkit")
    except ImportError as error:
        raise ConfigError(
            "pywhatkit is not installed; run: pip install .[notify]"
        ) from error
    pywhatkit.sendwhatmsg_instantly(
        phone, text, wait_time=constants.SEND_WAIT_SECONDS, tab_close=True
    )


class WhatsAppNotifier:
    """Notifier that sends to one phone number."""

    def __init__(self, phone: str) -> None:
        """Keep the recipient.

        @param phone The recipient in international format.
        """
        self._phone = phone

    def send_message(self, text: str) -> None:
        """Send one message."""
        send_message(text, self._phone)
