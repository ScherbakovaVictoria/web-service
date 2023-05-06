
from typing import List, Union
from fastapi import Query
from pydantic import BaseModel, Field, EmailStr
import datetime 



class GetPlaceInformation(BaseModel):
    id:int =  Query()
    name:str
    phone:str
    email:EmailStr
    description:str
    address:str
    rating:float
    photos: List[str]
    admin_id:int 
   
class UpdatePlaceInformation(BaseModel):
    id: int
    name:str
    phone:str
    email:EmailStr
    description:str
    address:str
    photos: List[str] 