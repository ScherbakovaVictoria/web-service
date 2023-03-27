from sqlalchemy import Column
from sqlalchemy import ForeignKey

from sqlalchemy import Integer, DateTime, Enum, DECIMAL
import datetime 
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Order(Base):
    __tablename__='order'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    ship_date = Column(DateTime, default=datetime.datetime.utcnow)
    cancel_date = Column(DateTime, default=datetime.datetime.utcnow)
    cancel_reason = Column(Integer())
    address = (Enum())
    shipping_type = (Integer())
    shipping_price = (DECIMAL())

    user_id = Column(Integer, ForeignKey('user.id'))
    payment_type = (Integer())


    transaction = relationship("Transaction")
    order_product = relationship("Order_product")

