from sqlalchemy import Column
from sqlalchemy import Integer, Enum
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Tag(Base):
    __tablename__='tag'
    id = Column(Integer, primary_key=True)
    name = Column(Enum(20))

    product_tag =  relationship('Product_tag')
