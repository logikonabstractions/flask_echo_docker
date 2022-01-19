import os
import logging
from utils import LOG_FOLDER

def get_root_logger(loggername, filename=None):
    """
    :param loggername: obv.
    :param filename: name of file where we want to output if we want a file handler.
    :return: the logger object from logging

    **Usage:** From anywhere in the project
    from logger import logger

    ``LOG = logger.get_root_logger(os.environ.get('ROOT_LOGGER', 'root'), filename=log_file)``

    then juste do ``LOG.error(...), LOG.info(...)`` as you would with the original logging.info() etc.

    The updside being we have decoupled the code from the actual logging lib used.


    """

    logger = logging.getLogger(loggername)
    debug = os.environ.get('ENV', 'development') == 'development'
    logger.setLevel(logging.DEBUG if debug else logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s:%(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if filename:
        file_handler = logging.FileHandler(os.path.join(LOG_FOLDER, filename))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


