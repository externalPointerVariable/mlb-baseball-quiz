from fastapi import APIRouter, Depends, Request, HTTPException
from authlib.integrations.starlette_client import OAuth
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.config import settings
from app.db import get_db
from app.models.user import User
from app.core.security import create_access_token

router = APIRouter()

# Configure OAuth for Google
oauth = OAuth()
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    client_kwargs={'scope': 'openid email profile'}
)

@router.get("/google/login")
async def google_login(request: Request):
   
    redirect_uri = request.url_for("google_callback")
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/google/callback")
async def google_callback(
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    try:
        # Retrieve token and userinfo from Google
        token = await oauth.google.authorize_access_token(request)
        userinfo = token.get("userinfo")
        if not userinfo:
            raise HTTPException(status_code=400, detail="Failed to retrieve user info from Google.")

        # Extract user information
        email = userinfo.get("email")
        name = userinfo.get("name")
        picture = userinfo.get("picture")  # Optional, if you want to store profile pictures

        if not email:
            raise HTTPException(status_code=400, detail="Email not provided by Google.")

        # Check if user exists in the database
        result = await db.execute(select(User).filter(User.email == email))
        user = result.scalar_one_or_none()

        if not user:
            # Create new user
            user = User(
                email=email,
                name=name,
                hashed_password="",  # Leave empty or set a placeholder for social login
                favorite_team="",    # Optional: Set default values
                favourite_player="", # Optional: Set default values
                xp=0,
                level=1
            )
            db.add(user)
            await db.commit()
            await db.refresh(user)

        # Generate a secure JWT token for the user
        access_token = create_access_token({"sub": user.email})
        return {
            "message": "Authentication successful",
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "picture": picture,
            },
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Authentication failed: {str(e)}")
