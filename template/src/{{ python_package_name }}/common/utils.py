"""Logging utilities."""
import logging
import os
from logging.handlers import TimedRotatingFileHandler

from rich.console import Console
from rich.logging import RichHandler


LOG_DIR = "log"
CONSOLE = Console(stderr=True)


def get_logger(name: str = "{{ python_package_name }}") -> logging.Logger:
    """Generate logger."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    os.makedirs(LOG_DIR, exist_ok=True)
    # file handler
    fh = TimedRotatingFileHandler(os.path.join(LOG_DIR, f"{name}.log"), 'midnight', backupCount=7)
    fh.setLevel(level=logging.DEBUG)
    # console handler
    sh = RichHandler(console=CONSOLE)
    sh.setLevel(level=logging.INFO)
    # formatter
    formatter = logging.Formatter(
        "[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
    )
    fh.setFormatter(formatter)
    # add handlers
    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger
