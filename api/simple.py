
import datetime

from flask import Blueprint, jsonify


BP = Blueprint("simple", __name__, url_prefix="/simple")


@BP.route("/")
def index():
    return jsonify({"data": "ok"})


@BP.route("/ping")
def ping():
    return jsonify({"ping": "pong"})


@BP.route("/now")
def now():
    dt_now = datetime.datetime.now()
    return jsonify({"datetime": dt_now})
