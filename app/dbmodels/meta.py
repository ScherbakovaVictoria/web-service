from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Enum
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Meta(Base):
    __tablename__='meta'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer(), ForeignKey('product.id'))
    type = Column(Enum())
    key = Column(Enum(50))
    value = Column(Enum(255))
