from app import db

class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    city = db.Column(db.String(64))
    country = db.Column(db.String(64))
    phone = db.Column(db.String(64))

    @staticmethod
    def create(id, first_name, last_name, city, country, phone):
        customer_dict = dict(
            id = id,
            first_name = first_name,
            last_name = last_name,
            city = city,
            country = country,
            phone = phone
        )
        customer_obj = Customer(**customer_dict)
        db.session.add(customer_obj)
        db.session.commit()    