from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTStrategy, BearerTransport, AuthenticationBackend
from app.models.user import UserCreate, UserUpdate, UserRead
from db import get_user_db, User
from config import SECRET

# Define BearerTransport
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

# JWT Strategy
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

# Authentication Backend
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

# FastAPI Users
fastapi_users = FastAPIUsers[User, int](
    get_user_db,
    [auth_backend],
)

# Current User dependency
current_user = fastapi_users.current_user(active=True)
