
from fastapi import HTTPException
from app import app, engine
from sqlalchemy.orm import Session
from app.db_models.Category import Category
from app.db_models.restourant_model import Place
from app.db_models.Order import Order, Position
from app.db_models.Client import Client, User
from app.db_models.Product import Product
from app.pydantic_models.other_pd_model import OrderPdModel
from app.controllers.recommend import *



@app.get('/recom')
def get_recom_for_user(user_id: int):
    with Session(engine) as session:
        rm = session.query(RecommendationModel).filter_by(user_id=user_id).first()
        print(rm.neighbour_id)

