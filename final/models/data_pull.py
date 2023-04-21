from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from sqlalchemy import Boolean, Column, Date, Integer, Numeric, String

from ..app.database import db


@dataclass
class DataPull(db.Model):
    __tablename__='data_pulls'

    hshd_num: int
    basket_num: int
    date: date
    product_num: int
    department: str
    commodity: str
    spend: Decimal
    units: int
    store_region: str
    week_num: int
    year: int
    loyalty_flag: bool
    age_range: str
    marital_status: str
    income_range: str
    homeowner_desc: str
    hshd_composition: str
    hshd_size: int
    children: int

    hshd_num = Column(Integer, primary_key=True)
    basket_num = Column(Integer, primary_key=True)
    date = Column(Date)
    product_num = Column(Integer, primary_key=True)
    department = Column(String(30))
    commodity = Column(String(30))
    spend = Column(Numeric(8,2))
    units = Column(Integer)
    store_region = Column(String(8))
    week_num = Column(Integer)
    year = Column(Integer)
    loyalty_flag = Column(Boolean, nullable=False)
    age_range = Column(String(5))
    marital_status = Column(String(10))
    income_range = Column(String(30))
    homeowner_desc = Column(String(10))
    hshd_composition = Column(String(30))
    hshd_size = Column(Integer)
    children = Column(Integer)
