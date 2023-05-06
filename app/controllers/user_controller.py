import hashlib
from urllib.request import Request
from app import app
from app import config
from pydantic import BaseModel, Field
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.responses import JSONResponse
from fastapi import Query, HTTPException
from app.pydantic_models import user_pd_model, other_pd_model
from app.db_models import Client as user_model
from app.db_models import db_init
from app.controllers import restoraunt_controller
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Query, Request, Response, status, HTTPException, Depends
from app import lifetime, engine
from sqlalchemy.orm import Session


def generate_password_hash(password:str):
    '''
    Метод генерирует хэш пароля 
    '''
    salt = b'\x1c\xc5\xc1\xee\t\r\'\xff\xf2\xf4\x12\x1c\xa2\xc9\x98\xa1\xb7\xff}\x05k"A]3\xe18\'\xd6\xb2[P'
    key = hashlib.pbkdf2_hmac('sha256', password.encode(
        'utf-8'), salt, 100000, dklen=128)
    return key
    

def check_password(password:str, password_hash:str):
    '''
    Проверка соотвествия хэша пароля хэшу в базе данных
    '''
    current_key = generate_password_hash(password)
    if current_key == password_hash:
        return True
    else:
        return False


class Settings(BaseModel):
    authjwt_secret_key: str = "secret"
    authjwt_access_token_expires = lifetime

@AuthJWT.load_config
def get_config():
    return Settings()

    
# Перехватчик исключений библиотеки JWT
@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )



@app.get('/v1/auth/login', description='Авторизация пользователя', tags=['Аворизация'])
def login(credentials: HTTPBasicCredentials = Depends(HTTPBasic())):
    try:
        user = user_model.User.get_by_login(login=credentials.username)
        if (check_password(password=credentials.password, password_hash=user.password_hash)):
            access_token = AuthJWT().create_access_token(subject=credentials.username)
            refresh_token =  AuthJWT().create_refresh_token(subject=credentials.username)
            return {"access_token": access_token, "refresh_token": refresh_token,
            "id":user.id, "lifetime":config.lifetime}
        else:
            raise HTTPException(status_code=401,detail="Bad username or password")
    except(db_init.NotFoundExeption): 
        raise HTTPException(status_code=404, detail="User not found")
    


@app.get('/v1/auth/refresh_access_token', description='Авторизация пользователя', tags=['Аворизация'])
def refresh_access_token(Authorize: AuthJWT = Depends()):
    """
    The jwt_refresh_token_required() function insures a valid refresh
    token is present in the request before running any code below that function.
    we can use the get_jwt_subject() function to get the subject of the refresh
    token, and use the create_access_token() function again to make a new access token
    """
    Authorize.jwt_refresh_token_required()
    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}


@app.post('/v1/client/create', description='Контроллер регистрации клиента', response_model=other_pd_model.Status,
tags=['Cleint object'])
def register_client(client: user_pd_model.UserRegister):
    try:
        user_model.Client.create(client)
        status_msg = other_pd_model.Status()
        status_msg.status = 'success'
        return status_msg
    except(db_init.ExistExeption):
        raise HTTPException(status_code=409, detail="User exist")
        


@app.get('/v1/client/get_profile', description='Получение профиля клиента', tags=['Cleint object'])
def get_clients_profile(id: int=Query(default=1, description='id пользователя в системе')):
    try:
        client_db = user_model.Client.get_by_id(id)
        return user_pd_model.GetUserProfile(firstname=client_db.firstname, phone_number=client_db.phone,
        email=client_db.email)
    except(db_init.NotFoundExeption):
        raise HTTPException(status_code=404, detail="Item not found")


@app.get('/v1/admin/get_profile', description='Получение профиля администратора', tags=['Admin object'])
def get_admin_profile(id: int=Query(default=1, description='id пользователя в системе')):
    with Session(engine) as session:
        client_db = session.query(user_model.User).get(id)
        return user_pd_model.GetAdminProfile(firstname=client_db.firstname, phone_number=client_db.phone,
        email=client_db.email, place_id=client_db.place[-1].id)
        

        
       
        
   

@app.put('/v1/client/update_profile', description='Обновление информации о клиенте', tags=['Cleint object'])
def update_clients_profile(profile: user_pd_model.UpdateUserProfile):
    try:
        user_model.Client.update(profile)
        status_msg = other_pd_model.Status()
        status_msg.status = 'success'
        return status_msg.status
    except(db_init.NotFoundExeption):
        HTTPException(status_code=404, detail='Not found')




@app.delete('/v1/client/delete_profile', description=' Удаление профиля клиента', tags=['Cleint object'])
def delete_clients_profile(id:int):
    with Session(engine) as session:
        client_db = session.query(user_model.Client).get(id)
        session.delete(client_db)
        session.commit()
        return({'status':'success'})



@app.post('/v1/admin/create', description='Контроллер регистрации администратора', response_model=other_pd_model.Status,
tags=['Admin object'])
def register_admin(client: user_pd_model.UserRegister):
    try:
        user_model.Admin.create(client)
        admin = user_model.Admin.get_by_login(login=client.phone_number)
        restoraunt_controller.create_place_template(admin.id)
        status_msg = other_pd_model.Status()
        status_msg.status = 'success'
        return status_msg
    except(db_init.ExistExeption):
        raise HTTPException(status_code=409, detail="User exist")