from fastapi import APIRouter , Depends , HTTPException , status
from schemas import usercreate , usersee
from sqlalchemy.orm import Session
from database import gt_db
from pwdlib import PasswordHash
from model import user
from jose import jwt , JWTError
from datetime import datetime , timedelta , timezone
from config import coonfig
#Xxpier_token_time , seRect_key , aLGORITHM  
from fastapi.security import OAuth2PasswordRequestForm
hashed = PasswordHash.recommended()

# injam 2 fuctasion mikhad
# yki brasakht v code krdn token
# yki bra hash krdn password user

userRouter = APIRouter(
    prefix="/user", 
    tags=["userthings"]
)

@userRouter.post("/")
def loging(usc:OAuth2PasswordRequestForm = Depends(), uscd:Session=Depends(gt_db)):
    # یا میتونستم فرمشو پایدانتیک کانورت کنم که اونم دیکشنریه با کی های یوزنیم و پسورد
    # hashedpass= hashed.hash(usc.password)
    # usc.password = hashedpass
    #detail = user(**usc.model_dump())
    # "userid" : detail.id in bra vgti bud ja request form as form pydantic estfade mikrdm
    payload = {"email" : usc.username  ,  "exp" : datetime.now(timezone.utc) + timedelta(minutes=coonfig.Xxpier_token_time)}
    token=jwt.encode(payload , algorithm=coonfig.aLGORITHM , key=coonfig.seRect_key )
    databaseuser = uscd.query(user).filter(user.email == usc.username).first()
    if databaseuser is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="wronge cerditnesal")
    # {detail.id} same as above
    if hashed.verify(usc.password,databaseuser.password):
        return f"sussvsfuly verify vzhmanni here email & id : {usc.username} +  and tokern for our server : {token}"
    else:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="wronge cerditnesal")
    
    #timedelta(minutes=Xxpier_token_time)+(datetime.now())
    
    
    
    
@userRouter.post("/firstfootstep")
def create(usc:usercreate, uscd:Session=Depends(gt_db)):
    hashedpass= hashed.hash(usc.password)
    usc.password = hashedpass
    detail = user(**usc.model_dump())
    uscd.add(detail)
    uscd.commit()
    uscd.refresh(detail)
    return f"sucssfuly creat account with {detail.email} and id : {detail.id}"