
from pydantic import BaseModel , EmailStr , ConfigDict

class post(BaseModel):
    topic:str
    content:str
    tags:list[str]

    model_config = ConfigDict(from_attributes=True)

class usersee(BaseModel):
    id:int
    email:EmailStr

class usercreate(BaseModel):
    email:EmailStr
    password : str
