# db.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from config import DATABASE_URL

# Initialize the database connection
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

database = Database(DATABASE_URL)
Base = declarative_base()

class User(Base, SQLAlchemyBaseUserTable):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)

async def get_user_db():
    yield SQLAlchemyUserDatabase(User, database)

# Create the async engine and session local
async_engine = create_async_engine(DATABASE_URL)
async_session_local = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)
