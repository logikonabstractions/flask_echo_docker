from flask import Flask
from flask import request
import time
from logger import get_root_logger
import requests
import os

app     = Flask(__name__)
NAME = os.environ["FLASK_NAME"]
PROJNAME = os.environ['COMPOSE_PROJECT_NAME']
LOG = get_root_logger("mylogger", filename=f'{NAME}.logs')
LOG.info(f'ENV VARS: {NAME} ')
LOG.info(f'Docker compose network name: {PROJNAME}')

envars = os.environ
for k,v in envars.items():
    LOG.info(f"{k} : {v}")

@app.route("/")
def home():
    try:
        value = request.args.get("foo")
    except Exception as ex:
        value = None

    LOG.info(f"{NAME} ping received with arg {value}")

    LOG.info("pinging other server.... ")

    if NAME == 'web_1':
        requests.get(f"http://web_2:5000/fromserver?foo={value if value else NAME}")
    else:
        requests.get(f"http://web_1:5000/fromserver?foo={value if value else NAME}")

    # ping the other server
    # requests.get("0.0.0.0:8001/from_server?foo=80")


    return "request successful!"

@app.route("/fromserver")
def from_server():
    try:
        value = request.args.get("foo")
    except Exception as ex:
        value = None

    LOG.info(f"{NAME} got from twin server: {value}")

    return "ping registered"

