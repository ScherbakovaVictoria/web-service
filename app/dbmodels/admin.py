from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Admin(Base):
    __tablename__='admin'
    id = Column(Integer, primary_key=True)
    name = Column(String())
    phone = Column(String())
    email = Column(String())
    description = Column(String())
    
    role = relationship("Role")
    product = Column()

    transaction = relationship("Transaction")
    favorites = relationship("Favorites")
    cart = relationship("Cart")
    review = relationship("Review")
    review_rating = relationship("Review_rating")


