import json
import base64
from . import db, http_auth
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
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
            "id": self.user_id,
            "name": self.name,
            "password_hash": self.password_hash,
            "email": self.email,
        }

    @staticmethod
    def serialize_list(user):
        json_users = []
        for user in user:
            json_users.append(user.serialize)
        return json_users

    def __repr__(self):
        return "<User %r>" % self.email


class Admin(db.Model):
    __tablename__ = "admin"
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
    def serialize_list(admin):
        json_admins = []
        for admin in admin:
            json_items.append(admin.serialize)
        return json_admins

    def __repr__(self):
        return "<Admin %r>" % self.email

class Item(db.Model):
    __tablename__ = "item"
    item_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    photo = db.Column(db.LargeBinary, nullable=False)
    # price in cents
    price = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    inventory_count = db.Column(db.Integer, nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"), nullable=False)

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            "id": self.item_id,
            "title": self.title,
            "description": self.description,
            "photo": self.photo,
            "price": self.price,
            "date": self.date,
            "inventory_count": inventory_count,
            "admin_id": self.admin_id,
        }

    @staticmethod
    def serialize_list(item):
        json_items = []
        for i in item:
            json_items.append(t.serialize)
        return json_items

    def __repr__(self):
        return "<Item%r>" % self.title

        class Item(db.Model):
    __tablename__ = "item"
    item_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    photo = db.Column(db.LargeBinary, nullable=False)
    # price in cents
    price = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    inventory_count = db.Column(db.Integer, nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"), nullable=False)

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            "id": self.item_id,
            "title": self.title,
            "description": self.description,
            "photo": self.photo,
            "price": self.price,
            "date": self.date,
            "inventory_count": inventory_count,
            "admin_id": self.admin_id,
        }

    @staticmethod
    def serialize_list(item):
        json_items = []
        for i in item:
            json_items.append(t.serialize)
        return json_items

    def __repr__(self):
        return "<Item%r>" % self.title

class Item(db.Model):
    __tablename__ = "item"
    item_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    photo = db.Column(db.LargeBinary, nullable=False)
    # price in cents
    price = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    inventory_count = db.Column(db.Integer, nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"), nullable=False)

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            "id": self.item_id,
            "title": self.title,
            "description": self.description,
            "photo": self.photo,
            "price": self.price,
            "date": self.date,
            "inventory_count": inventory_count,
            "admin_id": self.admin_id,
        }

    @staticmethod
    def serialize_list(item):
        json_items = []
        for i in item:
            json_items.append(t.serialize)
        return json_items

    def __repr__(self):
        return "<Item%r>" % self.title


class Payment(db.Model):
    __tablename__ = "payment"
    payment_id = db.Column(db.Integer, primary_key=True)
    # total amount in cents
    total_amt = db.Column(db.Integer, nullable=False)
    pdate = db.Column(db.Date, nullable=False)
    shipping_addr = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)
    

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            "id": self.item_id,
            "title": self.title,
            "description": self.description,
            "photo": self.photo,
            "price": self.price,
            "date": self.date,
            "inventory_count": inventory_count,
            "admin_id": self.admin_id,
        }

    @staticmethod
    def serialize_list(item):
        json_items = []
        for i in item:
            json_items.append(t.serialize)
        return json_items

    def __repr__(self):
        return "<Item%r>" % self.title