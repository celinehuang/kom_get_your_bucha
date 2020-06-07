import datetime
import re
from flask import Flask, jsonify, request, abort, make_response
from sqlalchemy import extract
from . import users
from .. import db, http_auth
from app.models import User

# get all users
@users.route("", methods=["GET"])
# @http_auth.login_required
def get_all_users():
    users = User.query.all()
    return jsonify(User.serialize_list(users))


# get user by ID
@users.route("/<int:user_id>", methods=["GET"])
@http_auth.login_required
def get_user_by_id(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if user is None:
        abort(404, "No user found with specified ID")
    return jsonify(user.serialize)


# get user by email
@users.route("/<email>", methods=["GET"])
# @http_auth.login_required
def get_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    if user is None:
        abort(404, "No user found with specified email")
    return jsonify(user.serialize)


# update a user's account details
@users.route("/<int:user_id>/profile", methods=["PUT"])
@http_auth.login_required
def update_user_details(user_id):

    data = request.get_json(force=True)

    user = User.query.filter_by(user_id=user_id).first()
    if user is None:
        abort(404, "No user found with specified ID")

    try:
        shipping_addr = data.get("shipping_addr")
    except TypeError:
        shipping_addr = None

    try:
        name = data.get("name")
    except TypeError:
        name = None

    if name is None and shipping_addr is None:
        abort(400, "No values given to update")

    if shipping_addr is not None:
        user.shipping_addr = shipping_addr
    elif name is not None:
        user.name = name
    else:
        user.shipping_addr = shipping_addr
        user.name = name

    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize)
