# Configure log file in overwriting mode

import logging

logging.basicConfig(filename='log2.txt', level=logging.INFO, filemode='w')

print("logging Demo")

logging.critical('This is a critical message')
logging.error('This is an error message')
logging.warning('This is a warning message')
logging.info('This is an info message')
logging.debug('This is a debug message')
