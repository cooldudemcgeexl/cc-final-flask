from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from sqlalchemy import Column, Date, Integer, Numeric, String

from ..app.database import db


@dataclass
class Transaction(db.Model):
    __tablename__ = 'transactions'

    hshd_num: int
    basket_num: int
    date: date
    product_num: int
    spend: Decimal
    units: int
    store_region: str
    week_num: int
    year: int


    hshd_num = Column(Integer,primary_key=True,nullable=False)
    basket_num = Column(Integer,primary_key=True, nullable=False)
    date = Column(Date)
    product_num = Column(Integer, primary_key=True)
    spend = Column(Numeric(8,2))
    units = Column(Integer)
    store_region = Column(String(8))
    week_num = Column(Integer)
    year = Column(Integer)