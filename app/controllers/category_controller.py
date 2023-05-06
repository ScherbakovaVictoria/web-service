
from fastapi import HTTPException
from app import app, engine
from sqlalchemy.orm import Session
from app.db_models.Category import Category
from app.db_models.restourant_model import Place


@app.post('/v1/category', tags=['Категирии'])
def create_category(name:str, place_id:int):
    with Session(engine) as session:
        place = session.query(Place).get(place_id)
        if name in place.categories: raise HTTPException(status_code=409,
            detail=f'Category exist',)
        else:    
            category = Category(name=name, place_id=place.id)
            place.categories.append(category)
            session.add(place)
            session.commit()
        
    return {'status':'success'}
    
@app.get('/v1/categories_by_placeid', tags=['Категирии'])
def get_categories_by_placeid(place_id:int):
    with Session(engine) as session:
        place = session.query(Place).get(place_id)
        category = list(place.categories)
        category_dict = {}
        for i in range(len(category)):
            category_dict[i] = category[i]
    return {"categories":category}

@app.delete('/v1/category', tags=['Категирии'])
def delete_category(id:int):
    with Session(engine) as session:
        category = session.query(Category).get(id)
        if category==None:
            raise HTTPException(status_code=404,
            detail=f'Category not found',)
        
        session.delete(category)
        session.commit()
    return {'status':'success'}