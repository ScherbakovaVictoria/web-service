from typing import Union, List
from pydantic import BaseModel, Field
import datetime 


class Status(BaseModel):
    
    status: Union[str, None] = Field(
        default=None, title="Статус запроса", min_length=1, description='ok'
    )
   

class PositionPdmodel(BaseModel):
    position_id: int
    count: int

class OrderPdModel(BaseModel):
    user_id: int
    positions: List[PositionPdmodel]
    address_of_delivery: str