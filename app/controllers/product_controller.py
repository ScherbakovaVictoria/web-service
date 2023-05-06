from fastapi import HTTPException
from app import app, engine
from app.pydantic_models.product_pd_models import CreateProductPdModel
from sqlalchemy.orm import Session
from app.db_models.Category import Category
from app.db_models.Product import Product
from app.db_models.Media import Photo
from app.db_models.restourant_model import Place

@app.post('/v1/product', tags=['Продукт'])
def create_product(product: CreateProductPdModel):
    with Session(engine) as session:
        category = session.query(Category).get(product.category_id)
        if category==None:
            raise HTTPException(status_code=404,
            detail=f'Category not found',)
        product_db = session.query(Product).filter_by(name=product.name).first()
        if product_db!=None:
            raise HTTPException(status_code=409,
            detail=f'Product exist',)
        
        product_db = Product(name=product.name, description=product.description,
                          price=product.price, category_id=category.id)
        session.add(product_db)
        session.commit()
    return {'status':'success'}

@app.delete('/v1/product')
def delete_product(id:int):
    with Session(engine) as session:
        product = session.query(Product).get(id)
        photo = session.query(Photo).filter_by(product_id=product.id).first()
        if photo!=None:
            session.delete(photo)
        session.delete(product)
        # TODO НАдо удалять файл из файловой системы
        session.commit()


@app.get('/v1/get_all_products_by_placeid')
def get_all_products_by_placeid(place_id:int):
    with Session(engine) as session:   
        place = session.query(Place).get(place_id)
        categories = list(place.categories)
        
        return categories
        

