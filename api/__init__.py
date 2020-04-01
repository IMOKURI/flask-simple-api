
from flask import Flask, jsonify


APP = Flask(__name__)


from api import simple

APP.register_blueprint(simple.BP)


@APP.errorhandler(404)
def error_not_found(_):
    return jsonify({"error": "404"}), 404
