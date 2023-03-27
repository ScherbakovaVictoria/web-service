from pydantic import BaseModel, Field, EmailStr
import datetime

class UserRegister(BaseModel):
    first_name: Union(str, None) = Field(
        default = ' ', title='The description of the item', min_length=1
    )