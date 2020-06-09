import datetime
import re
from flask import Flask, jsonify, request, abort, make_response
from sqlalchemy import extract
from . import admins
from .. import db, http_auth
from app.models import Admin


# get all admins
@admins.route("", methods=["GET"])
# @http_auth.login_required
def get_all_admins():
    admins = Admin.query.all()
    return jsonify(Admin.serialize_list(admins))


# get admin by ID
@admins.route("/<int:admin_id>", methods=["GET"])
@http_auth.login_required
def get_admin_by_id(admin_id):
    admin = Admin.query.filter_by(admin_id=admin_id).first()
    if admin is None:
        abort(404, "No admin found with specified ID")
    return jsonify(admin.serialize)
