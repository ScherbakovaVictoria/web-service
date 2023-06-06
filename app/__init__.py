
from fastapi import FastAPI
from starlette.config import Config # импорт класса для работы с переменными окружения
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


config = Config()
DATABASE_URL = config("EE_DATABASE_URL", cast=str, default="sqlite:///data.db")
STATIC_FOLDER_URL = config("STATIC_FOLDER_URL", cast=str, default=os.getcwd()+'/app/static/')
MAIN_ADDRESS = config("MAIN_ADDRESS", cast=str, default='localhost')
MEDIA_SERVER_ADDRESS = config("MEDIA_SERVER_ADDRESS", cast=str, default='http://localhost:8080/static/')



engine = create_engine(
    "sqlite:///data.db",  connect_args={"check_same_thread": False}
)

lifetime = 3600*5

Base = declarative_base()
app=FastAPI()








from app.db_models import Product, Category, Media, Client, Recommendation
from app.controllers import category_controller, product_controller, user_controller, order_controller, recommendation_controller


