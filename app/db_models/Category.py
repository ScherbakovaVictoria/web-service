



from app import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__='categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    products = relationship('Product', backref='category', lazy='joined')
    place_id = Column(Integer, ForeignKey('places.id'))
    
