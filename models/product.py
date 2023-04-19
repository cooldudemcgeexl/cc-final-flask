from sqlalchemy import Boolean, Column, Integer, String

from ..app.database import db


class Product(db.Model):
    __tablebame__ = 'products'

    product_num = Column(Integer, primary_key=True)
    department = Column(String(30))
    commodity = Column(String(30))
    brand_type = Column(String(10))
    natural_organic = Column(Boolean)