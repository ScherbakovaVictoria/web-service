from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, DECIMAL
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Order_product(Base):
   
    order_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    product_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))

    price = Column(DECIMAL)
    discount = Column(float())
    total = Column(Integer())