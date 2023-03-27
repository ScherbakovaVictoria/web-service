from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
class Role(Base):
    admin_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    admin_id = Column(Integer, ForeignKey('admin.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
