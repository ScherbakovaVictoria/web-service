from sqlalchemy import Column
from sqlalchemy import ForeignKey

from sqlalchemy import Integer, DateTime, String, DECIMAL
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Hall(Base):
    __tablename__='hall'
    id = Column(Integer, primary_key=True)
    number_table = Column(Integer())
    
    user_id = Column(Integer, ForeignKey('user.id'))
    organization = Column(Integer, ForeignKey('organization.id'))

