from app import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class RecommendationModel(Base):
    __tablename__='recommendation'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    neighbour_id = Column(Integer)