from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Product_tag(Base):
    product_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    tag_id = Column(Integer, primary_key=True)
    tag_id = Column(Integer, ForeignKey('tag.id'))
    