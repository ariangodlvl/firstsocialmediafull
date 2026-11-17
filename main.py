from fastapi import FastAPI
from post import postrouter
from user import userRouter
app = FastAPI()

app.include_router(postrouter)
app.include_router(userRouter)