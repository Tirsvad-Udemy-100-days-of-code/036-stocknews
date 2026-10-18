"""WhatsApp sender built on pywhatkit, an optional dependency."""

import importlib
from collections.abc import Callable

from stocknews import constants
from stocknews.domain.errors import NotificationError


def send_message(text: str, phone: str) -> None:
    """Send a message to a phone number with WhatsApp Web.

    pywhatkit opens WhatsApp Web in the default browser, which must be logged
    in, and presses send.

    @param text The message.
    @param phone The recipient in international format, like +4512345678.
    @throws NotificationError when pywhatkit is not installed.
    """
    try:
        pywhatkit = importlib.import_module("pywhatkit")
    except ImportError as error:
        raise NotificationError(
            "pywhatkit is not installed; run: python -m pip install -e .[whatsapp]"
        ) from error
    pywhatkit.sendwhatmsg_instantly(
        phone_no=phone,
        message=text,
        wait_time=constants.WHATSAPP_WEB_WAIT_SECONDS,
        tab_close=True,
        close_time=constants.WHATSAPP_WEB_CLOSE_SECONDS,
    )


class WhatsAppNotifier:
    """Notifier that sends to one phone number."""

    def __init__(
        self,
        phone: str,
        send: Callable[[str, str], None] = send_message,
    ) -> None:
        """Keep the recipient.

        @param phone The recipient in international format, with a leading +.
        @param send Sends one message as (text, phone); by default pywhatkit.
        """
        self._phone: str = phone.strip()
        self._send: Callable[[str, str], None] = send

    def send_message(self, text: str) -> None:
        """Send one message.

        @param text The message.
        @throws NotificationError when the number has no leading +, pywhatkit is
            missing or the send fails; the text never contains the number.
        """
        if not self._phone.startswith("+"):
            raise NotificationError(
                f"Setting {constants.ENV_PHONE_NUMBER} must start with + and the "
                "country code."
            )
        try:
            self._send(text, self._phone)
        except NotificationError:
            raise
        except Exception as error:  # third-party browser automation raises many types
            raise NotificationError(
                f"WhatsApp Web could not send the message ({type(error).__name__}); "
                "is the browser logged in to WhatsApp Web?"
            ) from error
