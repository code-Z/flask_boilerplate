from flask import Flask
from flask_pymongo import PyMongo

import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(level=logging.INFO)

app = Flask("hedwig")
mongo = PyMongo(app)
app.config.from_object("config")

handler = RotatingFileHandler(
    filename = app.config["LOG_FILE"], 
    maxBytes = app.config["LOG_MAX_BYTES"], 
    backupCount = app.config["LOG_BACKUP_COUNT"]
)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# from app.mod_mailer.routes import mod_mailer
# app.register_blueprint(mod_mailer)

@app.errorhandler(404)
def not_found(error):
    print(error)
    return "404 - Not found"