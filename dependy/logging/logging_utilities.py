import logging
import logging.handlers

DEFAULT_LOG_NAME = 'dependy_errors.log'
DEFAULT_LOG_SIZE = 5000000
DEFAULT_N_BACKUPS = 5

def get_null_logger():
    logger = logging.getLogger('dependy')
    logger.addHandler(logging.NullHandler())
    return logger

def get_dependy_logger():
    logger = logging.getLogger('dependy')
    logger.setLevel(logging.DEBUG)
    handler = logging.handlers.RotatingFileHandler(DEFAULT_LOG_NAME,
                                                   maxBytes=DEFAULT_LOG_SIZE,
                                                   backupCount=DEFAULT_N_BACKUPS)
    formatter = logging.Formatter('%(asctime)s (%(levelname)s) %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger