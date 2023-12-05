from fastapi import APIRouter, Depends
from app.db.database import get_db
from app.services.accounts import AccountService
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer
from app.schemas.accounts import AccountOut, AccountUpdate
from fastapi.security import HTTPBearer
from app.core.security import auth_scheme
from fastapi.security.http import HTTPAuthorizationCredentials


router = APIRouter(tags=["Account"], prefix="/me")
auth_scheme = HTTPBearer()


@router.get("/", response_model=AccountOut)
def get_my_info(
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    return AccountService.get_my_info(db, token)


@router.put("/", response_model=AccountOut)
def edit_my_info(
        updated_user: AccountUpdate,
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    return AccountService.edit_my_info(db, token, updated_user)


@router.delete("/", response_model=AccountOut)
def remove_my_account(
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    return AccountService.remove_my_account(db, token)
