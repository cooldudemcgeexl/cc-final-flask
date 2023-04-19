from dataclasses import dataclass

from sqlalchemy import Boolean, Column, Integer, String

from ..app.database import db


@dataclass
class Product(db.Model):
    __tablename__ = 'products'

    product_num: int
    department: str
    commodity: str
    brand_type: str
    natural_organic: bool

    product_num = Column(Integer, primary_key=True)
    department = Column(String(30))
    commodity = Column(String(30))
    brand_type = Column(String(10))
    natural_organic = Column(Boolean)