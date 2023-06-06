import numpy as np 
from fastapi import HTTPException
from app import app, engine
from sqlalchemy.orm import Session
from app.db_models.Category import Category
from app.db_models.restourant_model import Place
from app.db_models.Order import Order, Position
from app.db_models.Client import Client, User
from app.db_models.Product import Product
from app.db_models.Recommendation import RecommendationModel
from app.pydantic_models.other_pd_model import OrderPdModel
import math

def get_cosine_distance(vector1, vector2):
    chislitel = 0
    znamenatel = 0
    for key in (vector1.keys()):
        chislitel += vector1[key]*vector2[key]
    a1 = 0
    for key in (vector1.keys()):
        a1 += vector1[key]**2
    a2 = 0
    for key in (vector2.keys()):
        a2 += vector2[key]**2
    return chislitel/(np.sqrt(a1)*np.sqrt(a2))

def get_user_vector_preference(user_id:int):
    categories_id = [1,2,3,4,5,6]
    category_list=[]
    vector_preference = {}
    with Session(engine) as session:
        user = session.query(Client).get(user_id)
        for order in user.orders:
            for position in order.positions:
                product = session.query(Product).get(position.position_id)
                if product==None: continue
                for i in range(position.count):
                    category_list.append(product.category.id)
        for id in categories_id:
            vector_preference[str(id)] = category_list.count(id)
    return vector_preference
                
class UsersVector:
    def __init__(self, user_id, cosine_distance):
        self.user_id = user_id
        self.cosine_distance = cosine_distance

                
def get_the_best_vector(user_id:int, user_perf_vectors: dict):
    v1 = get_user_vector_preference(user_id=user_id)
    list_user_pref=[]
    for key in user_perf_vectors.keys():
        cosine_distance=get_cosine_distance(v1, user_perf_vectors[key])
        if math.isnan(cosine_distance):
            continue
        list_user_pref.append(UsersVector(user_id=int(key), cosine_distance=cosine_distance))
    list_sorted = sorted(list_user_pref, key=lambda user_vect: user_vect.cosine_distance)
    if len(list_sorted)<2:
        return -1
    return list_sorted[-2].user_id 
    
    
    
    


def scheduler():
    print('scheduler task started')
    with Session(engine) as session:
        users = session.query(Client).all()
        recom = session.query(RecommendationModel).all()
        for item in recom:
            session.delete(item)
        session.commit()
        user_perf_vectors = {}
        for user in users:
            user_perf_vectors[user.id] = get_user_vector_preference(user.id)
        for user in users:
            n_id = get_the_best_vector(user_id=user.id, user_perf_vectors=user_perf_vectors)
            rec = RecommendationModel(user_id=user.id, neighbour_id=n_id)
            session.add(rec)
            session.commit()
      
                    
                    
           