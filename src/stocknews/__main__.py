"""Run the program with python -m stocknews."""

import sys

from stocknews.presentation.cli import main

__all__ = ["main"]

if __name__ == "__main__":
    sys.exit(main())
