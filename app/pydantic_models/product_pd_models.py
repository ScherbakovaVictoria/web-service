
from pydantic import BaseModel, Field


class CreateProductPdModel(BaseModel):
    category_id:int = Field(default=1, title="Имя категории", description='ok')
    name:str =  Field(default='Латте', title="Имя продукта", min_length=1, description='ok')
    description: str = Field(default='Какой же вкусный кофе', title="Описание", min_length=1, description='ok')
    price:float = Field(default=100.0, title="Цена",  description='ok')
    photo: str = Field(default='jfgjkdfhjkfkjsfjlkdsjflks.png', title="Имя файла", min_length=1, description='ok')

