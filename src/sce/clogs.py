import logging

# Create custom logger logging all five levels
logger = logging.getLogger(__name__)

format  = "[{levelname:^9s}]"
f       = "| {asctime} :: {message}"
reset   = '\33[0m'

FORMATS = {
    logging.DEBUG:    format + f,
    logging.INFO:     f'\33[34m{format}\33[0m{f}', 
    logging.WARNING:  f'\33[33m{format}\33[0m{f}',
    logging.ERROR:    f'\33[31m{format}\33[0m{f}',
    logging.CRITICAL: f'\33[1m\33[31m{format}\33[0m{f}'
}

class CustomFormatter(logging.Formatter):

    def format(self, record):
        log_fmt = FORMATS[(record.levelno)] + reset
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
    logger.debug('This is an debug-level message')
    logger.info('This is an info-level message')
    logger.warning('This is an warning-level message')
    logger.error('This is an error-level message')