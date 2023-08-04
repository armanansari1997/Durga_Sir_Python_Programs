from custlogger import get_custom_logger
import logging


def f1():
    logger = get_custom_logger(logging.DEBUG)
    logger.critical('This is critical a message')
    logger.error('This is an error message')
    logger.warning('This is a warning message')
    logger.info('This is an info message')
    logger.debug('This is a debug message')


def f2():
    logger = get_custom_logger(logging.ERROR)
    logger.critical('This is critical a message')
    logger.error('This is an error message')
    logger.warning('This is a warning message')
    logger.info('This is an info message')
    logger.debug('This is a debug message')


def f3():
    logger = get_custom_logger(logging.CRITICAL)
    logger.critical('This is critical a message')
    logger.error('This is an error message')
    logger.warning('This is a warning message')
    logger.info('This is an info message')
    logger.debug('This is a debug message')


f1()
f2()
f3()
