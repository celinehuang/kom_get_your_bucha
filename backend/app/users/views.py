import datetime
import re
from flask import Flask, jsonify, request, abort, make_response
from sqlalchemy import extract
from . import users
from .. import db, http_auth
from app.models import User

# get all users
@users.route("", methods=["GET"])
@http_auth.login_required
def get_all_users():
    users = User.query.all()
    return jsonify(User.serialize_list(users))


# get user by ID
@users.route("/<int:user_id>", methods=["GET"])
@http_auth.login_required
def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        abort(404, "No user found with specified ID")
    return jsonify(user.serialize)


# get user by email
@users.route("/<email>", methods=["GET"])
@http_auth.login_required
def get_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    if user is None:
        abort(404, "No user found with specified email")
    return jsonify(user.serialize)


# update a user's profile
# TODO: allow users to change password
@users.route("/<int:user_id>/profile", methods=["PUT"])
@http_auth.login_required
def update_user_settings(user_id):
    data = request.get_json(force=True)

    try:
        shipping_addr = int(data.get("shipping_addr"))
    except TypeError:
        shipping_addr = None

    user = User.query.filter_by(id=user_id).first()
    if user is None:
        abort(404, "No user found with specified ID")

    user.shipping_addr = shipping_addr

    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize)
