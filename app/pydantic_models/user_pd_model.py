from typing import Union
from fastapi import Query
from pydantic import BaseModel, Field, EmailStr
import datetime 


class UserRegister(BaseModel):
    firstname: Union[str, None] = Field(
        default='Виктория', title="The description of the item", min_length=1
    )
    email:EmailStr
    phone_number:Union[str, None] = Query(
        default='89081488980', min_length=11, max_length=11
    )
    password: Union[str, None] = Field(
        default='11111111', title="The description of the item", min_length=8) 
    
    
class GetUserProfile(BaseModel):
    firstname: Union[str, None] = Field(
        default='Виктория', title="The description of the item", min_length=1
    )
    email:EmailStr
    phone_number:Union[str, None] = Query(
        default='89081488980', min_length=11, max_length=11
    )


class GetAdminProfile(BaseModel):
    firstname: Union[str, None] = Field(
        default='Виктория', title="The description of the item", min_length=1
    )
    email:EmailStr
    phone_number:Union[str, None] = Query(
        default='89081488980', min_length=11, max_length=11
    )
    place_id:int

class UpdateUserProfile(BaseModel):
    id: int
    firstname: Union[str, None] = Field(
        default='Виктория', title="The description of the item", min_length=1
    )
    email:EmailStr
    phone_number:Union[str, None] = Query(
        default='89081488980', min_length=11, max_length=11
    )