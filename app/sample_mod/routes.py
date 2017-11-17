from flask import Blueprint, request, jsonify
from app import app


sample_mod = Blueprint("sample", __name__, url_prefix="/sample")


# Sample route for demonstration
@mod_mailer.route("/sample", methods=["GET"])
def sample_route():
    app.logger.warning("A warning occured")
    app.logger.error("An error occured")
    app.logger.info("Info should be printed here")
    return "foo"