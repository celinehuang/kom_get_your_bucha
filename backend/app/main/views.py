from flask import Flask, jsonify, request, abort, make_response
from . import main
from app.email import send_email


@main.route("/", methods=["GET"])
def index():
    return "Welcome to the store!"


@main.route("/send-email", methods=["POST"])
def send_mail():
    # get email recipients and subject from the POST request
    data = request.get_json(force=True)
    recipients = data.get("recipients")
    subject = data.get("subject")

    if recipients is None or subject is None:
        abort(400, "Recipient(s) and subject cannot be empty")

    send_email(recipients, subject)
    return "message sent!"
