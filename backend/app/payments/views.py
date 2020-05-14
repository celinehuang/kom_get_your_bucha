from flask import Flask, jsonify, request, abort, make_response
from . import payments
from .. import db, http_auth
from app.models import Payment


# get all payments for user
@payments.route("/user/<int:user_id>", methods=["GET"])
@http_auth.login_required
def get_payments_for_user(user_id):
    payments = Payment.query.filter_by(user_id=user_id).all()
    return jsonify(Payment.serialize_list(payment))
