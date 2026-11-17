from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from database import gt_db 
from model import posts , tags
from schemas import post,usersee
from authrezision import verifu_user
postrouter = APIRouter(
    prefix="/post",
    tags=["post"]
)

@postrouter.get("/")
def mainsee(gt:Session = Depends(gt_db)):
    re = gt.query(posts).all()
    return re

@postrouter.post("/")
def upload(peload: post , uepeload : Session = Depends(gt_db) , tuken:str=Depends(verifu_user)):
    newpeload=posts(**peload.model_dump(exclude={"tags"}))
    for name in set(peload.tags):
        tag = uepeload.query(tags).filter(tags.name == name).first()
        if tag == None:
            tag = tags(name= name)
        newpeload.tags.append(tag)
    uepeload.add(newpeload)
    uepeload.commit()
    uepeload.refresh(newpeload)
    return uepeload

@postrouter.put("/{id}")
def edit(peload : post, id:int ,uepeload : Session = Depends(gt_db),tuken:str=Depends(verifu_user)):
    #newpeload=posts(**peload.model_dump())
    didi = dict(**peload.model_dump(exclude={"tags"}))

    yafteha = uepeload.query(posts).filter(posts.id == id).first()
    puttags = []
    for name in set(peload.tags):
        tag = uepeload.query(tags).filter(tags.name == name).first()
        if tag == None:
            tag = tags(name= name)
        puttags.append(tag)
    yafteha.tags = puttags
    for key , value in didi.items():
        setattr(yafteha, key,value)
    uepeload.commit()
    uepeload.refresh(yafteha)
    return yafteha

@postrouter.delete("/{id}")
def delet(id:int, deltodatabase:Session = Depends(gt_db),tuken:str=Depends(verifu_user)):
    yafteha = deltodatabase.query(posts).filter(posts.id == id).first()
    deltodatabase.delete(yafteha)
    deltodatabase.commit()
    return f"susscsfuly delete post with id {id}"

@postrouter.get("/personal")
def unpoblicedpost():
    pass

@postrouter.get("/{id}")
def spceficpost(id:int, pidakrdnpdnoepost:Session = Depends(gt_db),tuken:str=Depends(verifu_user)):
    yaheftm = pidakrdnpdnoepost.query(posts).filter(posts.id == id).first()
    return yaheftm