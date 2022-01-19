from flask import Flask
from flask import request
import os

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
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if filename:
        file_handler = logging.FileHandler(os.path.join(LOG_FOLDER, filename))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger





app     = Flask(__name__)
NAME = os.environ.get("FLASK_NAME")
flask_app = os.environ.get("FLASK_APP")
PORT = os.environ.get("PORT")
PROJNAME = os.environ.get('COMPOSE_PROJECT_NAME')
print(f"flask app: {flask_app}")
LOG = get_root_logger("mylogger", filename=f'{NAME}.logs')
LOG.info(f'ENV VARS: {NAME} ')
LOG.info(f'ENV VARS: {PORT} ')
LOG.info(f'Docker compose network name: {PROJNAME}')

envars = os.environ
for k,v in envars.items():
    LOG.info(f"{k} : {v}")

@app.route("/",  methods = ['POST'])
def calculate_returns(*args, **kwargs):
    # LOG.info("Flask endpoint for json POST")
    try:
        data = request.get_json(force=True)
        # LOG.info(f"data received: {data}")
        rate = data["interest_rates"]
        amount = data["initial_amount"]
        client = data["client"]
        prediction = [amount]
        for x in range(0,10):
            next_year = prediction[x]*(1+rate)
            prediction.append(next_year)
        response_data = {"10_years":prediction, "message":f"Many thanks for your business {client}"}
        return response_data
    except Exception as ex:
        return f"Couldn't parse this - {ex}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)