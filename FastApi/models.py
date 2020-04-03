from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from flask_login import  UserMixin
import uuid
from app.database.database import Base


class User(UserMixin,Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(64),)
    username = Column(String(64), )
    role = Column(String(64), )
    password_hash = Column(String(128))
    head_img = Column(String(128), )
    create_time  = Column(DateTime,default=datetime.now)

    def __repr__(self):
        return '<User %r>' % self.username

# 文章表
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    title=Column(String(32))
    author =Column(String(32))
    img_url = Column(Text,nullable=False)
    content=Column(Text,nullable=False)
    tag=Column(String(64),nullable=True)
    uuid = Column(Text,default="12345523453455")
    desc = Column(String(100), nullable=False)
    create_time = Column(DateTime,default=datetime.now)
    articleDetail = relationship('Article_Detail', backref='article')

    def __repr__(self):
        return '<Article %r>' % self.title


class Article_Detail(Base):
    __tablename__ = 'article_detail'
    id = Column(Integer, primary_key=True)
    d_content=Column(Text,nullable=False)
    uid = Column(Integer, ForeignKey('article.id'))

    def __repr__(self):
        return '<Article_Detail %r>' % self.uid

class Global_V(Base):
    __tablename__ = 'global_V'
    id = Column(Integer, primary_key=True)
    desc = Column(String(64), nullable=False,default="记录网站访问量")
    count= Column(Integer,nullable=False,default=1)
    create_time = Column(DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return '<Global_V %r>' % self.desc

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    theme = Column(String(64), nullable=False,default="评论主题")
    content = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False)
    uuid = Column(Text,nullable=False)
    create_time = Column(DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return '<Comment %r>' % self.theme
