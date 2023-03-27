from fastapi import FastAPI

app = FastAPI()

from app import app
from app.controllers import user_controller
from app.controllers import 