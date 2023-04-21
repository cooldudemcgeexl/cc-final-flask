from dataclasses import dataclass

from sqlalchemy import Boolean, Column, Integer, String

from ..app.database import db


@dataclass
class Household(db.Model):
    __tablename__ = 'households'
    hshd_num: int
    loyalty_flag: bool
    age_range: str
    marital_status: str
    income_range: str
    hshd_size: int
    homeowner_desc: str
    hshd_composition: str
    children: int

    hshd_num = Column(Integer, primary_key=True, nullable=False)
    loyalty_flag = Column(Boolean, nullable=False)
    age_range = Column(String(5))
    marital_status = Column(String(10))
    income_range = Column(String(30))
    homeowner_desc = Column(String(10))
    hshd_composition = Column(String(30))
    hshd_size = Column(Integer)
    children = Column(Integer)

