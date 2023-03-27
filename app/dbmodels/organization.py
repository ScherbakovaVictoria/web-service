from sqlalchemy import Column
from sqlalchemy import ForeignKey

from sqlalchemy import Integer, DateTime, String, DECIMAL, FLOAT
import datetime 
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Order(Base):
    __tablename__='order'
    id = Column(Integer, primary_key=True)
    name = Column(String())
    address = (String())
    phone = (String())
    description = Column(String())
    rating = Column(FLOAT())
    user_id = Column(Integer, ForeignKey('user.id'))
    hall = 
    categotia = 


    transaction = relationship("Transaction")
    order_product = relationship("Order_product")

