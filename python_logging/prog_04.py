# How to write exception information to the log file

import logging

logging.basicConfig(filename='mylog27072022.log', level=logging.INFO, filemode='w',
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')

logging.info('A new request came')

try:
    x = int(input('Enter 1st number'))
    y = int(input('Enter 2nd numebr'))
    print('The result', x/y)
except ZeroDivisionError as msg:
    print('Cannot divide with zero')
    logging.exception(msg)
except ValueError as msg:
    print('please provide int value only')
    logging.exception(msg)

logging.info('request processing completed')
