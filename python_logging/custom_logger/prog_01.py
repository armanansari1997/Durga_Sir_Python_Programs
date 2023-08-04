# Create Logger object & set Level

import logging

# step:1
logger = logging.getLogger('demologger')
logger.setLevel(logging.WARNING)

# step:2
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.ERROR)

# step:3
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                  datefmt='%d/%m/%Y %I:%M:%S %p')

# step:4
consoleHandler.setFormatter(formatter)

# step:5
logger.addHandler(consoleHandler)

# step:6
logger.critical('This is a critical message')
logger.error('This is an error message')
logger.critical('This is a critical message')
logger.info('This is an info message')
logger.debug('This is a debug message')
