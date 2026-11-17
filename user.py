from fastapi import APIRouter , Depends , HTTPException , status
from schemas import usercreate , usersee
from sqlalchemy.orm import Session
from database import gt_db
from pwdlib import PasswordHash
from model import user
from jose import jwt , JWTError
from datetime import datetime , timedelta , timezone
from authrezision import Xxpier_token_time , seRect_key , aLGORITHM  
hashed = PasswordHash.recommended()

# injam 2 fuctasion mikhad
# yki brasakht v code krdn token
# yki bra hash krdn password user

userRouter = APIRouter(
    prefix="/user", 
    tags=["userthings"]
)

@userRouter.get("/")
def loging(usc:usercreate, uscd:Session=Depends(gt_db)):
    hashedpass= hashed.hash(usc.password)
    usc.password = hashedpass
    detail = user(**usc.model_dump())
    if True:
        databaseuser = uscd.query(user).filter(user.email == detail.email).first
    else:
        raise HTTPException(status_code=sta404 , detail="wronge cerditnesal")
    
    if True:
        user.password == detail.password
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="wronge cerditnesal")
    
    #timedelta(minutes=Xxpier_token_time)+(datetime.now())
    
    payload = {"email" : detail.email  , "userid" : detail.id , "exp" : datetime.now(timezone.utc) + timedelta(minutes=Xxpier_token_time)}
    token=jwt.encode(payload , algorithm=aLGORITHM , key=seRect_key )
    return f"sussvsfuly verify vzhmanni here email & id : {detail.email} + {detail.id} and tokern for our server : {token}"
    
@userRouter.post("/firstfootstep")
def create(usc:usercreate, uscd:Session=Depends(gt_db)):
    hashedpass= hashed.hash(usc.password)
    usc.password = hashedpass
    detail = user(**usc.model_dump())
    uscd.add(detail)
    uscd.commit()
    uscd.refresh(detail)
    return f"sucssfuly creat account with {detail.email} and id : {detail.id}"