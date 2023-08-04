# # creating of generic logger and uses
import inspect
import logging


def get_custom_logger(level):
    function_name = inspect.stack()[1][3]
    logger_name = function_name + "logger"

    # step:1
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # step:2
    fileHandler = logging.FileHandler('abc.txt', mode='w')
    fileHandler.setLevel(logging.DEBUG)

    # step:3
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                      datefmt='%d/%m/%Y %I:%M:%S %p')

    # step:4
    fileHandler.setFormatter(formatter)

    # step:5
    logger.addHandler(fileHandler)

    return logger




