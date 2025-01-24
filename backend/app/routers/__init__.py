from .auth import router as auth_router
from .quiz import router as quiz_router
from .profile import router as profile_router  # Add this line

__all__ = ["auth_router", "quiz_router", "profile_router"]