from datetime import datetime
import os
from flask import Flask, jsonify, request, abort, make_response, redirect, current_app
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.utils import secure_filename
from sqlalchemy import extract
from . import items
from .. import db, http_auth
from app.models import User, Item, Payment, Admin


ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif"}

# app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024

# get all items
@items.route("", methods=["GET"])
def get_items():
    items = Item.query.all()
    return jsonify(Item.serialize_list(items))


@items.route("/classic", methods=["GET"])
def get_classic_items():
    items = Item.query.filter_by(item_type="classic")
    return jsonify(Item.serialize_list(items))


@items.route("/limited", methods=["GET"])
def get_limited_items():
    items = Item.query.filter_by(item_type="limited")
    return jsonify(Item.serialize_list(items))


@items.route("/alcoholic", methods=["GET"])
def get_alcoholic_items():
    items = Item.query.filter_by(item_type="alcoholic")
    return jsonify(Item.serialize_list(items))


@items.route("/equipment", methods=["GET"])
def get_equipment_items():
    items = Item.query.filter_by(item_type="equipment")
    return jsonify(Item.serialize_list(items))


# create new items (admin only)
@items.route("/create-item", methods=["POST"])
# @http_auth.login_required
def create_item():
    data = request.get_json(force=True)
    title = data.get("title")
    description = data.get("description")
    item_type = data.get("item_type")
    admin_id = data.get("admin_id")
    inventory_count = int(data.get("inventory_count"))
    price = int(data.get("price"))
    date = datetime.now()

    admin = Admin.query.filter_by(admin_id=admin_id).first()
    if admin is None:
        abort(404, "No admin found with specified ID")

    if (
        title == ""
        or description == ""
        or item_type == ""
        or inventory_count == ""
        or price is None
        or date is None
    ):
        abort(400, "Cannot have empty fields for item")

    new_item = Item(
        title=title,
        description=description,
        item_type=item_type,
        inventory_count=inventory_count,
        price=price,
        date=date,
        admin_id=admin.admin_id,
    )

    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.serialize)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# delete items (admin only)
@items.route("/<int:id>", methods=["DELETE"])
# @http_auth.login_required
def delete_item(id):
    item = Item.query.filter_by(item_id=id).first()
    if item is None:
        abort(404, "No item found with specified ID")

    db.session.delete(item)
    db.session.commit()

    return jsonify(item.serialize)


# get items by id
@items.route("/<int:id>", methods=["GET"])
# @http_auth.login_required
def get_item_by_id(id):
    item = Item.query.filter_by(item_id=id).first()
    if item is None:
        abort(404, "No item found with specified ID")

    return jsonify(item.serialize)


# update an item by ID (admin only)
@items.route("/<int:id>/update", methods=["PUT"])
# @http_auth.login_required
def update_item(id):
    data = request.form.to_dict(flat=True)
    title = data.get("title")
    description = data.get("description")
    item_type = data.get("item_type")
    try:
        photo = request.files["photo"]
    except KeyError:
        photo = None
    # admin_id = data.get("admin_id")
    inventory_count = data.get("inventory_count")
    price = data.get("price")
    date = datetime.now()

    # admin = Admin.query.filter_by(admin_id=admin_id).first()
    # if admin is None:
    #     abort(404, "No admin found with specified ID")

    item = Item.query.filter_by(item_id=id).first()
    if item is None:
        abort(400, "No item found with specified ID")

    if title is not None:
        item.title = title

    if description is not None:
        item.description = description

    if item_type is not None:
        item.item_type = item_type

    if inventory_count is not None:
        item.inventory_count = int(inventory_count)

    if price is not None:
        item.price = int(price)

    if photo is not None:
        if photo and allowed_file(photo.filename):
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
            file_path = "{}/{}".format(current_app.config["UPLOAD_FOLDER"], filename)
            item.photo = file_path

    if (
        title == ""
        and description == ""
        and photo is None
        and item_type == ""
        and inventory_count == ""
        and price is None
        and date is None
    ):
        abort(400, "No fields to update")

    item.date = date

    db.session.add(item)
    db.session.commit()
    return jsonify(item.serialize)


# update inventory count for list of items
@items.route("/update-inventory", methods=["PUT"])
@http_auth.login_required
def update_inventory():
    data = request.get_json(force=True)
    itemsInCart = data.get("inCart")

    uniqueIds = {}

    for item in itemsInCart:
        id = item["id"]
        inventory_count = item["inventory_count"]

        if id not in uniqueIds:
            uniqueIds[id] = 1
        else:
            uniqueIds[id] += 1

    for id in uniqueIds:
        item = Item.query.filter_by(item_id=id).first()
        item.inventory_count = item.inventory_count - uniqueIds[id]

    db.session.add(item)
    db.session.commit()
    return "Inventory updated successfully", 200
