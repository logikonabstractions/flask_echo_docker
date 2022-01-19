import requests, time
import random, json
import os
import logging
LOG_FOLDER = "logs"

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
    # console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if filename:
        file_handler = logging.FileHandler(os.path.join(LOG_FOLDER, filename))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger




PYWORKBOOK_ROOTURL = "http://python_workbook:5000/"

if __name__ == '__main__':
    LOG = get_root_logger("mylogger", filename=f'logs.logs')
    full_url = f"{PYWORKBOOK_ROOTURL}"
    go = True
    clients = ["Rachelle", "Billy", "Joey", "Monica"]
    while go:
        interest_rates = random.random()*(0.1)
        initial_amount = random.randrange(10000, 1000000)
        client = random.choice(clients)
        data = {"client": client, "initial_amount": initial_amount, "interest_rates":interest_rates}
        LOG.info(f"{client} places {initial_amount} at {interest_rates*10}% annually. PythonWorkbook calculates the returns...")

        response = requests.post(full_url, data=json.dumps(data))
        json_content = response.json()

        LOG.info(f"Your returns for the next 10 years:")
        LOG.info(json_content["10_years"])
        LOG.info(json_content["message"])
        LOG.info("")
        LOG.info("")
        time.sleep(3)