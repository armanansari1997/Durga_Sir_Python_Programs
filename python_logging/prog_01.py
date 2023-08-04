import logging

logging.basicConfig(filename='log1.txt', level=logging.WARNING)

print("logging Demo")

logging.critical('This is a critical message')
logging.error('This is an error message')
logging.warning('This is a warning message')
logging.info('This is an info message')
logging.debug('This is a debug message')
