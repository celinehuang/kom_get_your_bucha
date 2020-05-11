from datetime import datetime
import os
from flask import Flask, jsonify, request, abort, make_response, redirect
from werkzeug.utils import secure_filename
from sqlalchemy import extract
from . import payments
from .. import db, http_auth
from app.models import User, Item, Payment

UPLOAD_FOLDER = "./item-images"
ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

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


def allowed_image(filename):

    # We only want files with a . in the filename
    if not "." in filename:
        return False

    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

def allowed_image_filesize(filesize):

    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False

# upload item image (called inside of the create_item POST request)
@app.route("/upload-item-image", methods=["GET", "POST"])
def add_item_image():

      if request.method == "POST":

        if request.files:

            if "filesize" in request.cookies:

                if not allowed_image_filesize(request.cookies["filesize"]):
                    print("Filesize exceeded maximum limit")
                    return redirect(request.url)

                image = request.files["image"]

                if image.filename == "":
                    print("No filename")
                    return redirect(request.url)

                if allowed_image(image.filename):
                    filename = secure_filename(image.filename)

                    image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

                    print("Image saved")

                    return redirect(request.url)

                else:
                    print("That file extension is not allowed")
                    return redirect(request.url)

    return render_template("public/upload.html")


# get items in cart

# get items in payment
