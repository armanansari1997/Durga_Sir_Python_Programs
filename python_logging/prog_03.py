# How to format log files

import logging

# logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')


print("logging Demo")

logging.critical('This is a critical message')
logging.error('This is an error message')
logging.warning('This is a warning message')
logging.info('This is an info message')
logging.debug('This is a debug message')
