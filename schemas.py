
from pydantic import BaseModel , EmailStr

class post(BaseModel):
    topic:str
    content:str
    tags:list[str]

class usersee(BaseModel):
    id:int
    email:EmailStr

class usercreate(BaseModel):
    email:EmailStr
    password : str
