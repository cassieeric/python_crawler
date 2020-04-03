from typing import List
from starlette.templating import Jinja2Templates
from app import schemas, models
from app.database.database import get_db
from app.home import crud
from fastapi import Depends, HTTPException, Form
from sqlalchemy.orm import Session
from app.models import User
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException,Request
from fastapi.responses import RedirectResponse


userRouter = APIRouter()
templates = Jinja2Templates(directory="app/templates") # 模板目录

@userRouter.post("/login/", response_model=schemas.UserOut)
async def login(*,request: Request,db: Session = Depends(get_db), username: str = Form(None), password: str = Form(None),):
    if request.method == "POST":
        db_user = db.query(models.User).filter(User.username == username).first()
        if not db_user:
            raise HTTPException(status_code=400, detail="用户不存在")
        print("验证通过 ！！！")
        return RedirectResponse('/index')

    return templates.TemplateResponse("user/login.html", {"request": request})


async def userList(*,request: Request,db: Session = Depends(get_db)):
    userList = db.query(models.User).all()
    return templates.TemplateResponse("user/user-index.html", {"request": request,'userList':userList})

userRouter.add_api_route(methods=['GET','POST'],path="/login",endpoint=login,response_model=schemas.UserOut)
userRouter.add_api_route(methods=['GET','POST'],path="/list",endpoint=userList)
