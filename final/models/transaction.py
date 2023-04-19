from sqlalchemy import Boolean, Column, Date, Integer, Numeric, String

from ..app.database import db


class Transaction(db.Model):
    __tablename__ = 'transactions'

    hshd_num = Column(Integer,primary_key=True,nullable=False)
    basket_num = Column(Integer,primary_key=True, nullable=False)
    date = Column(Date)
    product_num = Column(Integer, primary_key=True)
    spend = Column(Numeric(8,2))
    units = Column(Integer)
    store_region = Column(String(8))
    week_num = Column(Integer)
    year = Column(Integer)