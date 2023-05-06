from app import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Photo(Base):
    __tablename__='photos'
    id = Column(Integer, primary_key = True)
    path = Column(String)
    place_id = Column(Integer, ForeignKey('places.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    #category_id
