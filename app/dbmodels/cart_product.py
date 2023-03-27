from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Cart_product(Base):
    __tablename__='cart_product'
    cart_id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey('cart.id'))
    product_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))

    quantity = Column(Integer())
