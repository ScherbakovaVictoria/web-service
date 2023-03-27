from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, Enum
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Category(Base):
    __tablename__='category_id'
    id = Column(Integer, primary_key=True)
    parent_category_id = Column(Integer, ForeignKey('category.id'))
    name = Column(Enum(20))
    photo_id = Column(Integer, ForeignKey('photo.id'))
    
    product_category =  relationship('Product_category')
    category =  relationship('Category')
    product =  relationship('Product')
    