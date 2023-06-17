import logging

# Create custom logger logging all five levels
logger = logging.getLogger(__name__)


class CustomFormatter(logging.Formatter):
    
    # green = '\u001b[32m'
    # grey = '\x1b[38;20m'
    # yellow = '\x1b[33;20m'
    # red = '\x1b[31;20m'
    # bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'
    
    # Define format for logs
    format = '[{levelname:^8s}] | {asctime} :: {message}'

    FORMATS = {
    # logging.DEBUG: grey + format + reset,
    logging.INFO: f'\u001b[32m' + format + reset,
    logging.WARNING: f'\x1b[33;20m' + format + reset,
    logging.ERROR: f'\x1b[31;20m' + format + reset,
    logging.CRITICAL: f'\x1b[31;1m' + format + reset
    }
    
    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, style='{')
        return formatter.format(record)
    
# Create stdout handler for logging to the console (logs all five levels)
handler = logging.StreamHandler()
handler.setFormatter(CustomFormatter())
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[handler],
)

if __name__ == '__main__':
    
    logger.info('This is an info-level message')
    # log.debug('This is an debug-level message')
    # log.warning('This is an warning-level message')