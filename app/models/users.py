from app import db
import uuid

from app.models.address import Address
from app.models.orders import Orders
from app.models.tickets import Tickets

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password = db.Column(db.String(64))
    contact = db.Column(db.String(64))
    addresses = db.relationship(Address, lazy=True, backref="user")
    orders = db.relationship(Orders, lazy=True, backref="user")
    tickets = db.relationship(Tickets, lazy=True, backref="user")

    @staticmethod
    def create(name, email, password, contact):

        user_dict = dict(
            guid = str(uuid.uuid4()),
            name = name,
            email = email,
            password = password,
            contact = contact
        )
        user_obj = Users(**user_dict)

        db.session.add(user_obj)
        db.session.commit()


    def update(self, **details_dict):
        for k,v in details_dict.items():
            setattr(self, k, v)
        db.session.commit()

    # def to_dict(self):
    #     return {
    #         "email": self.email,
    #         "password": self.password,
    #         "name": self.name
    #     }
