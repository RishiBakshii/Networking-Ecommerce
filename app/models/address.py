from app import db
import uuid

class Address(db.Model):
    __tablename__ = "address"
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String, nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    house_number = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)
    pin_code = db.Column(db.String)

    @staticmethod
    def create(user_id, house_number, city, state, country, pin_code):
        address_dict = dict(
            guid = str(uuid.uuid4()),
            user_id = user_id,
            house_number = house_number,
            city = city,
            state = state,
            country = country,
            pin_code = pin_code
        )
        address_obj = Address(**address_dict)
        db.session.add(address_obj)
        db.session.commit()

    def update(self, **details_dict):
        for k,v in details_dict.items():
            setattr(self, k, v)
        db.session.commit()