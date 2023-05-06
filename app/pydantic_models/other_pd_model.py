from typing import Union
from pydantic import BaseModel, Field
import datetime 


class Status(BaseModel):
    
    status: Union[str, None] = Field(
        default=None, title="Статус запроса", min_length=1, description='ok'
    )
   