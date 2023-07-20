from app import db
import uuid

from app.models.products import Products
from app.models.address import Address

class Orders(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String, nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    product = db.relationship(Products, lazy=True, uselist=False)
    quantity = db.Column(db.Integer)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    address = db.relationship(Address, lazy=True, uselist=False)
    amount = db.Column(db.Float)

    @staticmethod
    def create(user_id, product_id, quantity, address_id, amount):
        order_dict = dict(
            guid = str(uuid.uuid4()),
            user_id = user_id,
            product_id = product_id,
            quantity = quantity,
            address_id = address_id,
            amount = amount
        )
        order_obj = Orders(**order_dict)
        db.session.add(order_obj)
        db.session.commit()

    def update(self, **details_dict):
        for k,v in details_dict.items():
            setattr(self, k, v)
        db.session.commit()