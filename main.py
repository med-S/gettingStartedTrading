import os
from flask import Flask
import logging

app = Flask(__name__) # create Flask server
# get instance of logger and set log severity as defined by the cli parameter
logging.basicConfig(filename='myapp.log', level=logging.INFO)
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)

@app.route('/', methods=["GET"])
def hello():
    app.logger.debug('This is a DEBUG log record.')
    app.logger.info('This is an INFO log record.')
    app.logger.warning('This is a WARNING log record.')
    app.logger.error('This is an ERROR log record.')
    app.logger.critical('This is a CRITICAL log record.')
    print("TEST")
    return 'Hello Abdessamad, rak bkhayr! chabe3 ch3iiir, khedam mzn'
