from sqlalchemy import Boolean, Column, Integer, String

from ..app.database import db


class Household(db.Model):
    __tablename__ = 'households'
    
    hshd_num = Column(Integer, primary_key=True, nullable=False)
    loyalty_flag = Column(Boolean, nullable=False)
    age_range = Column(String(5))
    marital_status = Column(String(10))
    income_range = Column(String(30))
    hshd_size = Column(Integer)
    children = Column(Integer)