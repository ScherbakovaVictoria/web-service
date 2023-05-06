from app import Base
from sqlalchemy import  Column, Integer, String, Float, Date, ForeignKey

from sqlalchemy.orm import relationship




class Place(Base):
    __tablename__ = 'places'
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    phone = Column(String(120))
    email = Column(String(120))
    description = Column(String)
    address = Column(String)
    rating = Column(Float)
    categories = relationship('Category', backref='place', 
                             cascade="all,delete,delete-orphan", lazy='dynamic')
    photos = relationship('Photo', backref='place', 
                             cascade="all,delete,delete-orphan", lazy='dynamic')
    admin_id = Column(ForeignKey('users.id'))
    # orders 
    # feedBack
    


class Place_Tag(Base):
    __tablename__='place_tag'
    id = Column(Integer, primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id'))
    place_id = Column(Integer, ForeignKey('places.id'))

class Tag(Base):
    __tablename__='tags'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class FeedBack(Base):
    __tablename__='feedback'
    id = Column(Integer, primary_key=True)
    feedback_text = Column(String)
    mark = Column(Integer)
    place_id = Column(Integer, ForeignKey('places.id'))
    client_id = Column(Integer, ForeignKey('users.id'))
