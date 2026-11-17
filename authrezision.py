from fastapi import Depends
from sqlalchemy.orm import Session
from database import gt_db
from model import user
import jwt
from jwt.exceptions import InvalidTokenError
from fastapi.security import OAuth2AuthorizationCodeBearer
seRect_key = "CaFST0a9DBexPPxdCt9y3B4uDG4fxyGct6T9d0pS47faxScT6a" 
aLGORITHM = "HS256"
Xxpier_token_time = 90

def verify_token(token):
    re = jwt.decode(jwt=token , key=seRect_key , algorithms=aLGORITHM)
    return re
# 2 ta fuctasion to auth2 baied bnvisem 
# yki token decode lne
# yki user verfiy kne and idsho ps bde(brgrdone)

def verifu_user(tokene , ririyuser: Session=Depends(gt_db)):
    re = verify_token(tokene)
    email=re.get("email")
    yaftehverifyshode=ririyuser.query(user).filter(email==user.email).first()
    return yaftehverifyshode