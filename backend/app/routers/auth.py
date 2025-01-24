from fastapi import APIRouter, Depends, HTTPException, Request
from authlib.integrations.starlette_client import OAuth
from jose import jwt
from ..core import security
from ..models.user import User
from ..core.database import get_db
from ..core.config import settings
from sqlalchemy.orm import Session

router = APIRouter()

# OAuth configuration
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
    db: Session = Depends(get_db)  # Now properly typed
):
    try:
        token = await oauth.google.authorize_access_token(request)
        userinfo = token.get("userinfo")
        
        # Your existing user handling logic
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))