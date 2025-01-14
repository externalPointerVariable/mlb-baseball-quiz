from fastapi import FastAPI
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users import FastAPIUsers, models
from fastapi_users.authentication import CookieAuthentication
from fastapi_users.authentication.strategy.oauth2 import OAuth2AuthorizationCodeBearer
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from config import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, SECRET, DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: DeclarativeMeta = declarative_base()

class User(Base, models.BaseUser, models.BaseOAuthAccountMixin):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)

async def get_user_db():
    yield SQLAlchemyUserDatabase(User, SessionLocal())

oauth2_google = OAuth2AuthorizationCodeBearer(
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    token_url="https://oauth2.googleapis.com/token",
    redirect_uri="http://localhost:8000/auth/callback/google",
    scopes=["profile", "email"],
)

cookie_authentication = CookieAuthentication(secret=SECRET, lifetime_seconds=3600)

app = FastAPI()

fastapi_users = FastAPIUsers(
    get_user_db,
    [cookie_authentication, oauth2_google],
    User,
    UserCreate,
    UserUpdate,
    UserRead,
)

app.include_router(
    fastapi_users.get_auth_router(cookie_authentication), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(), prefix="/auth", tags=["auth"]
)
app.include_router(
    fastapi_users.get_oauth_router(oauth2_google, "google"), prefix="/auth/oauth", tags=["auth"]
)
app.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])
