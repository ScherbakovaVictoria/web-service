
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
import random



@app.get('/recom')
def get_recom_for_user(user_id: int):
    with Session(engine) as session:
        rm = session.query(RecommendationModel).filter_by(user_id=user_id).first()
        if rm==None:
            return {'status:':'no recommendation'}
        recommend_user = session.query(Client).filter_by(id=rm.neighbour_id).first()
        print(recommend_user.id)
        
        order =  recommend_user.orders[random.randint(0, len(recommend_user.orders)-1)] 
        position = order.positions[random.randint(0, len(order.positions)-1)]
        recommend_product = session.query(Product).filter_by(id=position.position_id).first()
        return(recommend_product)
        
        
        
        

