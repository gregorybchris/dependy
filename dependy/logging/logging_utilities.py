import functools
import logging
import logging.handlers


DEFAULT_LOG_NAME = 'dependy_errors.log'
DEFAULT_LOG_SIZE = 5000000
DEFAULT_N_BACKUPS = 5

logger_created = False


def get_null_logger():
    logger = logging.getLogger('dependy')
    logger.addHandler(logging.NullHandler())
    return logger


def get_logger():
    global logger_created
    logger = logging.getLogger('dependy')
    if not logger_created:
        logger.setLevel(logging.DEBUG)
        handler = logging.handlers.RotatingFileHandler(DEFAULT_LOG_NAME,
                                                       maxBytes=DEFAULT_LOG_SIZE,
                                                       backupCount=DEFAULT_N_BACKUPS)
        formatter = logging.Formatter('%(asctime)s.%(msecs)03d (%(levelname)s) %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger_created = True
    return logger


def log_context(name, context_tag='context_log'):
    logger = get_logger()

    def decorator(function):
        @functools.wraps(function)
        def func_wrapper(*args, **kwargs):
            logger.info(f"[{context_tag}] Start={name}")
            result = function(*args, **kwargs)
            logger.info(f"[{context_tag}] End={name}")
            return result
        return func_wrapper
    return decorator
