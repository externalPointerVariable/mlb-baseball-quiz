from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend
from app.models.user import UserCreate, UserUpdate, UserRead
from db import get_user_db, User
from config import SECRET

# JWT Strategy
jwt_strategy = JWTStrategy(secret=SECRET, lifetime_seconds=3600)

# Authentication Backend
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=None,
    get_strategy=jwt_strategy,
)

# FastAPI Users
fastapi_users = FastAPIUsers[User, int](
    get_user_db,
    [auth_backend],
)

# Current User dependency
current_user = fastapi_users.current_user()
