from app import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__='products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    photo = relationship('Photo', backref='product')
    category_id = Column(Integer, ForeignKey('categories.id'))