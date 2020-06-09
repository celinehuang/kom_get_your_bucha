from flask import Flask, jsonify, request, abort, make_response
from . import payments
from .. import db, http_auth
from app.models import Payment


# get all payments for user
# return items in the same payment_id
@payments.route("/user/<int:user_id>", methods=["GET"])
@http_auth.login_required
def get_payments_for_user(user_id):
    payments = Payment.query.filter_by(user_id=user_id).all()
    return jsonify(Payment.serialize_list(payment))


# create new order/ payment history
@payments.route("/create-order", methods=["POST"])
@http_auth.login_required
def create_order():
    data = request.get_json(force=True)
    user_id = data.get("user_id")
    item_id = data.get("item_id")
    shipping_addr = date.get("shipping_addr")
    total_amt = data.get("total_amt")
    pdate = datetime.now()

    user = User.query.filter_by(user_id=user_id).first()
    if user is None:
        abort(404, "No user found with specified ID")

    if (
        user_id is None
        or item_id is None
        or shipping_addr == ""
        or total_amt is None
        or pdate is None
    ):
        abort(400, "Cannot have empty fields for payment")

    new_payment = Payment(
        user_id=user_id,
        item_id=item_id,
        shipping_addr=shipping_addr,
        total_amt=total_amt,
        pdate=pdate,
    )

    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.serialize)
