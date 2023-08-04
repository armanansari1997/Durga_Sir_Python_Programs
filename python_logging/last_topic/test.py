import logging
import logging.config


logging.config.fileConfig('logging_config.init')

logger = logging.getLogger('demologger')
logger.critical('This is critical a message')
logger.error('This is an error message')
logger.warning('This is a warning message')
logger.info('This is an info message')
logger.debug('This is a debug message')
