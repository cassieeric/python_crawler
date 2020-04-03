from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:123456@127.0.0.1:3306/blog"
# 创建数据库连接URI


# 初始化
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)


# 创建DBSession类型
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    return SessionLocal()
