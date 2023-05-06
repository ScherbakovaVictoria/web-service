from app import app
from app.db_models import restourant_model
from app.db_models.Media import Photo 
from app.pydantic_models import restourant_pd_model
from sqlalchemy.orm import Session
from app import engine, config
from fastapi import Query, HTTPException
import os

def create_place_template(admin_id: int)->int:
    '''
    Метод создаёт шаблон заведения
    admin_id - id администратора в системе, обслуживающего заведение
        0  - успешное завершение функции
        -1 - функция завершена с ошибкой 
    '''
    with Session(engine) as session:
        place_template = restourant_model.Place(name = 'Название заведения', phone='88000000000',
        email = 'example@mail.ru', description = 'Шаблон описания заведения и его основного коцепта', 
        address = 'Воронеж, ул. Революции, д. 305', rating = 5.0, admin_id = admin_id)
        session.add(place_template)
        session.commit()
        return 0
    return -1

    


@app.put('/v1/place/update', tags=['Place object'])
def update_place(place_information: restourant_pd_model.UpdatePlaceInformation):
    print(place_information)
    with Session(engine) as session:
        place = session.query(restourant_model.Place).get(place_information.id)
        place.name = place_information.name
        place.email = place_information.email
        place.descroption = place_information.description
        place.address = place_information.address
        place.phone = place_information.phone
        newlist = place_information.photos
        oldlist = list(map(lambda x: x.filename, place.photos))
        for photo in oldlist:
            
            if not (config.MEDIA_SERVER_ADDRESS +photo in newlist):
                path = config.STATIC_FOLDER_URL+str(photo).split('/')[-1]
                if os.path.exists(path):
                    try:
                        os.remove(path)
                    except: pass
        for photo in place.photos:
            session.delete(photo)
        for photo in newlist:
            place.photos.append(Photo(path=photo.split('/')[-1], place_id = place.id))
           
            
        session.add(place)
        session.commit()
        return {"status":"success"}

@app.get('/v1/place/get', description='Возвращает основную инфорсмацию о заведении по его id', tags=['Place object'])
def get_place(id: int=Query(default=1, description='id заведения в системе')):
    with Session(engine) as session:
        place = session.query(restourant_model.Place).get(id)
        
        return restourant_pd_model.GetPlaceInformation(id=place.id, name=place.name,
        email=place.email, description=place.description, address=place.address, 
        phone = place.phone, admin_id=place.admin_id, rating=place.rating, photos=list(map(lambda x: config.MEDIA_SERVER_ADDRESS + x.filename, place.photos)))

        
        ## TODO Нужно сделать нормально
    