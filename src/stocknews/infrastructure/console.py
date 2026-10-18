"""Console notifier used in dry-run mode."""

import sys


class ConsoleNotifier:
    """Notifier that prints the message instead of sending it."""

    def send_message(self, text: str) -> None:
        """Print the message, replacing characters the console cannot show."""
        encoding = sys.stdout.encoding or "utf-8"
        safe = text.encode(encoding, errors="replace").decode(encoding)
        print(safe, end="\n\n")
