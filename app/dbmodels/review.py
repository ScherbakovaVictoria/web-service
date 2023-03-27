from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, DateTime, Enum, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
import datetime 

Base = declarative_base()

class Review(Base):
    __tablename__='review'
    id = Column(Integer, primary_key=True)
    
    product_id = Column(Integer, ForeignKey('product.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    date = Column(DateTime, default=datetime.datetime.utcnow)
    grade = Column(Integer())
    pros = Column(Enum())
    cons = Column(Enum())
    comment = Column(String())

    review_rating =  relationship('Review_rating')
