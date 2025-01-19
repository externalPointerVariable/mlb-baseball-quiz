from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from config import DATABASE_URL

database = Database(DATABASE_URL)
base = declarative_base()


class User(base, SQLAlchemyBaseUserTable):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)

async def user_regitration():
    yield SQLAlchemyUserDatabase(User, database)

async_engine = create_async_engine(DATABASE_URL, pool_pre_ping=True)
async_session = sessionmaker(bind = async_engine, expire_on_commit=False, class_= AsyncSession)