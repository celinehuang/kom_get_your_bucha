import json
import base64
from . import db, http_auth
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    shipping_addr = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expiration=86400):
        s = Serializer(current_app.config["SECRET_KEY"], expiration)
        return s.dumps({"token": self.user_id})

    @staticmethod
    @http_auth.verify_token
    def verify_auth_token(token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return False  # valid token, but expired
        except BadSignature:
            return False  # invalid token
        return User.query.get(data["token"])

    # @staticmethod
    # def generate_test_user():
    #     user = User(name="Albert Kragl", email="akragl@gmail.com", password="password")
    #     db.session.add(user)
    #     db.session.commit()
    #     return user

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "password_hash": self.password_hash,
            "email": self.email,
        }

    @staticmethod
    def serialize_list(users):
        json_users = []
        for user in users:
            json_users.append(user.serialize)
        return json_users

    def __repr__(self):
        return "<User %r>" % self.email


class Admin(db.Model):
    __tablename__ = "admins"
    admin_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expiration=86400):
        s = Serializer(current_app.config["SECRET_KEY"], expiration)
        return s.dumps({"token": self.id})

    @staticmethod
    @http_auth.verify_token
    def verify_auth_token(token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return False  # valid token, but expired
        except BadSignature:
            return False  # invalid token
        return User.query.get(data["token"])

    # @staticmethod
    # def generate_test_user():
    #     user = User(name="Albert Kragl", email="akragl@gmail.com", password="password")
    #     db.session.add(user)
    #     db.session.commit()
    #     return user

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            "id": self.admin_id,
            "name": self.name,
            "password_hash": self.password_hash,
            "email": self.email,
        }

    @staticmethod
    def serialize_list(admins):
        json_admins = []
        for admin in admins:
            json_admin.append(admin.serialize)
        return json_admins

    def __repr__(self):
        return "<Admin %r>" % self.emaila


class Item(db.Model):
    __tablename__ = "items"
    item_id = db.Column(db.Integer, primary_key=True)
    # classic, limited, alcoholic, equipment
    item_type = db.Column(db.String(64), nullable=False)
    title = db.Column(db.String(64), nullable=False)
    # ingredient list
    description = db.Column(db.String(256), nullable=False)
    # default image should be added
    photo = db.Column(db.LargeBinary)
    # price in cents
    price = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    inventory_count = db.Column(db.Integer, nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey("admins.admin_id"), nullable=False)

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            "id": self.item_id,
            "item_type": self.item_type,
            "title": self.title,
            "description": self.description,
            "photo": self.photo,
            "price": self.price,
            "date": self.date,
            "inventory_count": self.inventory_count,
            "admin_id": self.admin_id,
        }

    @staticmethod
    def serialize_list(items):
        json_items = []
        for i in items:
            json_items.append(i.serialize)
        return json_items

    def __repr__(self):
        return "<Item%r>" % self.item_id


class Payment(db.Model):
    __tablename__ = "payments"
    payment_id = db.Column(db.Integer, primary_key=True)
    # total amount in cents
    total_amt = db.Column(db.Integer, nullable=False)
    pdate = db.Column(db.Date, nullable=False)
    shipping_addr = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("items.item_id"), nullable=False)

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            "payment_id": self.payment_id,
            "total_amt": self.total_amt,
            "pdate": self.pdate,
            "shipping_addr": self.shipping_addr,
            "user_id": self.user_id,
            "item_id": self.item_id,
        }

    @staticmethod
    def serialize_list(payments):
        json_payments = []
        for p in payments:
            json_payments.append(p.serialize)
        return json_payments

    def __repr__(self):
        return "<Payment%r>" % self.payment_id
