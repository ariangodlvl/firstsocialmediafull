from fastapi import Depends
from sqlalchemy.orm import Session
from config import coonfig
#aLGORITHM , seRect_key
from database import gt_db
from model import user
import jwt
from jwt.exceptions import InvalidTokenError
from fastapi.security import OAuth2AuthorizationCodeBearer , OAuth2PasswordRequestForm , OAuth2PasswordBearer

bear = OAuth2PasswordBearer("bear")

def verify_token(token):
    re = jwt.decode(jwt=token , key=coonfig.seRect_key , algorithms=coonfig.aLGORITHM)
    return re
# 2 ta fuctasion to auth2 baied bnvisem 
# yki token decode lne
# yki user verfiy kne and idsho ps bde(brgrdone)

#tokene : str Depends(bear)
def verifu_user(tokene , ririyuser: Session=Depends(gt_db)):
    re = verify_token(tokene)
    email=re.get("email")
    yaftehverifyshode=ririyuser.query(user).filter(email==user.email).first()
    return yaftehverifyshode