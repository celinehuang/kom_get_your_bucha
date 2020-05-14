from datetime import datetime
import os
from flask import Flask, jsonify, request, abort, make_response, redirect
from werkzeug.utils import secure_filename
from sqlalchemy import extract
from . import items
from .. import db, http_auth
from app.models import User, Item, Payment, Admin

UPLOAD_FOLDER = "./item-images"
ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif"}
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
# app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024

# get all items
@items.route("/get-items", methods=["GET"])
@http_auth.login_required
def get_items():
    items = Item.query.all()
    return jsonify(Item.serialize_list(items))


# create new items (admin only)
@items.route("/create-item", methods=["POST"])
# @http_auth.login_required
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
        or date is None
    ):
        abort(400, "Cannot have empty fields for item")

    admin = Admin.query.filter_by(email=email).first()
    if admin is None:
        abort(404, "Admin does not exist")

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


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# upload item image (called inside of the create_item POST request)
@items.route("/upload-item-image", methods=["POST"])
@http_auth.login_required
def add_item_image():
    if "file" not in request.files:
        abort(400, "No file sent in request!")

    file = request.files["file"]
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    file_path = "./item-images/{}".format(filename)
    # # detect all objects in original image
    # # returns a tuple: (OBJECT, FILE_PATH)
    # detected_objects = detect_objects(file_path)

    # object_tuples = []
    f = open("./imagenew.jpg", "rb")
    encoded_image = base64.b64encode(f.read())
    return jsonify(encoded_image.decode("utf-8"))


# get items in cart

# get items in payment
