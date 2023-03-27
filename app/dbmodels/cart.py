from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Cart(Base):
    __tablename__='cart_id'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('cart.id'))
    
    cart_product =  relationship('Cart_product')