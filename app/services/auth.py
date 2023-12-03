from fastapi import HTTPException, Depends, status
from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.models.models import User
from app.db.database import get_db
from app.core.security import verify_password, get_user_token, get_token_payload

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    if not verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    return await get_user_token(id=user.id)


async def get_refresh_token(token, db):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Invalid refresh token.", headers={"WWW-Authenticate": "Bearer"})

    payload = get_token_payload(token, credentials_exception)
    user_id = payload.get('id', None)
    if not user_id:
        raise credentials_exception

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise credentials_exception

    return await get_user_token(id=user.id, refresh_token=token)
