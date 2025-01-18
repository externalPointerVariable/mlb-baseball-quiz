# User Management and Authentication
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTStrategy, BearerTransport, AuthenticationBackend
from models.user import UserCreate, UserUpdate, UserRead
from db import get_user_db, User
from config import SECRET

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_db,
    [auth_backend],
)

current_user = fastapi_users.current_user(active=True)
