from datetime import datetime
from flask import Flask, jsonify, request, abort, make_response
from sqlalchemy import extract
from . import payments
from .. import db, http_auth
from app.models import User, Item, Payment

# get all items
@items.route("", methods=["GET"])
@http_auth.login_required
def get_items():
    items = Item.query.all()
    return jsonify(Item.serialize_list(items))


# create new items (admin only)
@items.route("", methods=["POST"])
@http_auth.login_required
def create_item():
    data = request.get_json(force=True)
    title = data.get("title")
    description = data.get("description")
    email = data.get("email")
    # photo = data.get("photo")
    iventory_count = int(data.get("inventory_count"))
    price = int(data.get("price"))
    date = datetime.now()

    if (
        title == ""
        or description == ""
        or email == ""
        # or photo is None
        or iventory_count == ""
        or price is None
        # or date is None
    ):
        abort(400, "Cannot have empty fields for item")

    user = User.query.filter_by(email=email).first()
    if user is None:
        abort(404, "User does not exist")

    new_item = Item(
        title=title,
        description=description,
        iventory_count=iventory_count,
        price=price,
        date=date,
        admin_id=admin.id,
    )

    db.session.add(new_item)
    db.session.commit()


# get items in cart

# get items in payment
