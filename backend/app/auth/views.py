import datetime
from flask import Flask, jsonify, request, abort, make_response
from . import auth
from .. import db, http_auth
from app.models import User, Admin, verify_auth_token

# log in an existing user
@auth.route("/login", methods=["POST"])
def login():
    """
    Required in body:
    email: String
    password: String
    """
    data = request.get_json(force=True)
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if (
        user is not None
        and user.password_hash is not None
        and user.verify_password(password)
    ):
        token = user.generate_auth_token()
        return jsonify({"user": user.serialize, "token": token.decode("ascii")})
    return "Wrong email or password!", 400


# check if token is valid and return user
@auth.route("/token", methods=["POST"])
def verify_token():
    """
    Required in body:
    token: String
    """
    data = request.get_json(force=True)
    token = data.get("token")

    user = verify_auth_token(token)
    if user is None:
        abort(404, "Token does not match any user")

    return jsonify(user.serialize)


# register a new user
@auth.route("/register", methods=["POST"])
def register():
    """
    Required in body:
    name: String
    email: String
    password: String
    """
    data = request.get_json(force=True)
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if name == "" or email == "" or password == "":
        abort(400, "Cannot have empty fields for user")

    user = User.query.filter_by(email=email).first()
    if user is not None:
        abort(400, "Account already exists with this email")

    new_user = User(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    token = new_user.generate_auth_token()
    return jsonify({"user": new_user.serialize, "token": token.decode("ascii")})


# register an admim
@auth.route("/register-admin", methods=["POST"])
def register_admin():
    """
    Required in body:
    name: String
    email: String
    password: String
    """
    data = request.get_json(force=True)
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if name == "" or email == "" or password == "":
        abort(400, "Cannot have empty fields for user")

    admin = Admin.query.filter_by(email=email).first()
    if admin is not None:
        abort(400, "Account already exists with this email")

    new_admin = Admin(name=name, email=email, password=password)
    db.session.add(new_admin)
    db.session.commit()
    return jsonify(new_admin.serialize)


# admin login
@auth.route("/admin-login", methods=["POST"])
def admin_login():
    """
    Required in body:
    email: String
    password: String
    """
    data = request.get_json(force=True)
    email = data.get("email")
    password = data.get("password")

    admin = Admin.query.filter_by(email=email).first()
    if (
        admin is not None
        and admin.password_hash is not None
        and admin.verify_password(password)
    ):
        token = admin.generate_auth_token()
        return jsonify({"admin": admin.serialize, "token": token.decode("ascii")})
    return "Wrong email or password!", 400


# log out an existing user
@auth.route("/logout")
@http_auth.login_required
def logout():
    return "Logged out successfully", 200


# update a user's password
@auth.route("/<int:user_id>/password", methods=["POST"])
# @http_auth.login_required
def change_password(user_id):
    """
    Required in body:
    old_password: String
    new_password: String

    """
    user = User.query.filter_by(user_id=user_id).first()
    if user is None:
        abort(404, "No user found with specified ID")

    data = request.get_json(force=True)
    old_password = data.get("old_password")
    new_password = data.get("new_password")

    if user.change_password(old_password, new_password):
        return "Password changed successfully", 200
    else:
        return "Failed to change password", 400
