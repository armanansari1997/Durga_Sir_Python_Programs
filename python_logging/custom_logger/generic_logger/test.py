from custlogger import get_custom_logger
import logging


def log_test():
    logger = get_custom_logger(logging.DEBUG)
    logger.critical('This is critical a message')
    logger.error('This is an error message')
    logger.warning('This is a warning message')
    logger.info('This is an info message')
    logger.debug('This is a debug message')


log_test()
