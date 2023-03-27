from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class User(Base):
    __tablename__='user_account'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20))
    surname = Column(String)
    gender = Column(Integer())
    addresses = Column(String())
    phone = Column(String())
    email = Column(String())
    description = Column(String())
    password_hash = Column(String())
    
    transaction = relationship("Transaction")
    favorites = relationship("Favorites")
    cart = relationship("Cart")
    review = relationship("Review")
    review_rating = relationship("Review_rating")

