# routers.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.auth import login
from app.schemas.auth import TokenResponse
from app.db.database import get_db
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router = APIRouter(tags=["Auth"], prefix="/auth")


@router.post("/login")
async def user_login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return await login(user_credentials, db)
