from typing import List
from fastapi import Depends, FastAPI, HTTPException
from starlette.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.home import user


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static") # 挂载静态文件，指定目录
templates = Jinja2Templates(directory="app/templates") # 模板目录


app.include_router(user.userRouter,prefix="/user")



