from app import db

from app.models.editor.supplier import Supplier

class CompanyProducts(db.Model):
    __tablename__ = "company_products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=False)
    unit_price = db.Column(db.Float)
    package = db.Column(db.String(64))
    is_discontinued = db.Column(db.Integer)

    @staticmethod
    def create(id, name, supplier_id, unit_price, package, is_discontinued):
        products_dict = dict(
            id = id,
            name = name,
            supplier_id = supplier_id,
            unit_price = unit_price,
            package = package,
            is_discontinued = is_discontinued
        )
        products_obj = CompanyProducts(**products_dict)
        db.session.add(products_obj)
        db.session.commit()