from app import db

from app.models.editor.company_orders import CompanyOrders
from app.models.editor.company_products import CompanyProducts

class OrderItems(db.Model):
    __tablename__ = "order_items"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('company_orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('company_products.id'), nullable=False)
    unit_price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    @staticmethod
    def create(id, order_id, product_id, unit_price, quantity):
        order_dict = dict(
            id = id,
            order_id = order_id,
            product_id = product_id,
            unit_price = unit_price,
            quantity = quantity
        )
        order_obj = OrderItems(**order_dict)
        db.session.add(order_obj)
        db.session.commit()