from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Review_rating(Base):
    review_id = Column(Integer, primary_key=True)
    review_id = Column(Integer, ForeignKey('review.id'))
    user_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    opinion = Column(Integer())
    