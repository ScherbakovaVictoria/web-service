from app import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.db_models.Product import Product


class Position(Base):
    __tablename__='position'
    id = Column(Integer, primary_key=True)
    count = Column(Integer)
    position_id = Column(Integer)
    order_id = Column(Integer, ForeignKey('orders.id'))


class Order(Base):
    __tablename__='orders'
    id = Column(Integer, primary_key=True)
    positions = relationship(Position)
    address_of_delivery = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
