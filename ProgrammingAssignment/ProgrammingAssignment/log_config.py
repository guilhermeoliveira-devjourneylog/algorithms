# log_config.py
from colorama import Fore, Style, init
import logging

# init(convert=True)

class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors"""
    grey = Style.DIM + Fore.WHITE
    green = Fore.GREEN
    yellow = Fore.YELLOW
    red = Fore.RED
    bold_red = Style.BRIGHT + Fore.RED
    reset = Style.RESET_ALL

    format = '%(asctime)s - %(levelname)s - %(message)s'

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, "%Y-%m-%d %H:%M:%S")
        return formatter.format(record)

def configure_logging():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()
    for handler in logger.handlers:
        handler.setFormatter(CustomFormatter())
