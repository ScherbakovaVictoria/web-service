

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

@app.post('/v1/order', tags=['Заказы'])
def create_order(order: OrderPdModel):
    with Session(engine) as session:
        orderDb = Order()
        orderDb.address_of_delivery = order.address_of_delivery
        orderDb.user_id = order.user_id
        session.add(orderDb)
        session.commit()
        session.refresh(orderDb)
        for item in order.positions:
            orderDb.positions.append(Position(count = item.count, position_id=item.position_id,
                                              order_id=orderDb.id))
        session.add(orderDb)
        session.commit()
        
    return {'status':'success'}



    
           

            

        
