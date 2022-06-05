import os

from flask import abort
from flask import Flask
from flask import jsonify
from flask import request
from pyjokes import get_joke


app = Flask(__name__)


def is_request_valid(request):
    is_token_valid = request.form["token"] == os.environ["SLACK_VERIFICATION_TOKEN"]
    return is_token_valid


@app.route("/tell-joke", methods=["POST"])
def tell_joke():
    if not is_request_valid(request):
        abort(400)

    return jsonify(
        response_type="in_channel",
        text=get_joke(language="en", category="neutral"),
    )
