# How to create custom logger

import logging


# step:1
logger = logging.getLogger('demologger')
logger.setLevel(logging.INFO)

# step:2
fileHandler = logging.FileHandler('abc.txt', mode='w')
fileHandler.setLevel(logging.INFO)

# step:3
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                  datefmt='%d/%m/%Y %I:%M:%S %p')

# step:4
fileHandler.setFormatter(formatter)

# step:5
logger.addHandler(fileHandler)

# step:6

logger.critical('This is critical a message')
logger.error('This is an error message')
logger.warning('This is a warning message')
logger.info('This is an info message')
logger.debug('This is a debug message')
