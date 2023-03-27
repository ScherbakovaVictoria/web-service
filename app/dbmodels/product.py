from sqlalchemy import Column
from sqlalchemy import ForeignKey

from sqlalchemy import Integer, DateTime, Enum, DECIMAL, FLOAT
import datetime 
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Product(Base):
    __tablename__='product'
    id = Column(Integer, primary_key=True)
    name = Column(Enum(50))
    price = Column(DECIMAL)
    discount = Column(FLOAT)

    category_id = (Integer, ForeignKey('category.id'))

    description = Column(Enum(255))
    quantity = (Integer())
    sku = Column(Enum)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    published_at = Column(DateTime, default=datetime.datetime.utcnow)

    favorites = relationship("Favorites")
    cart_product = relationship("Cart_product")
    product_category = relationship("Product_category")
    product_tag = relationship("Product_tag")
    meta = relationship("Meta")
    order_product = relationship("Order_product")
    review = relationship("Review")
    product_photo = relationship("Product_photo")
