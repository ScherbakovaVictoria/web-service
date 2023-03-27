from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class file(Base):
    photo_id = Column(Integer, primary_key=True)
    size = Column(Integer())
    file = Column(file())
    category =  relationship('Category')
    product_photo =  relationship('Product_photo')