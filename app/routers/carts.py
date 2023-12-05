from fastapi import APIRouter, Depends, Query, status
from app.db.database import get_db
from app.services.carts import CartService
from sqlalchemy.orm import Session
from app.schemas.carts import CartCreate, CartUpdate, CartOut, CartOutDelete, CartsOutList
from app.core.security import get_current_user
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials

router = APIRouter(tags=["Carts"], prefix="/carts")
auth_scheme = HTTPBearer()


# Get All Carts
@router.get("/", status_code=status.HTTP_200_OK, response_model=CartsOutList)
def get_all_carts(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Items per page"),
    token: HTTPAuthorizationCredentials = Depends(auth_scheme)
):
    return CartService.get_all_carts(token, db, page, limit)


# Get Cart By User ID
@router.get("/{cart_id}", status_code=status.HTTP_200_OK, response_model=CartOut)
def get_cart(
        cart_id: int,
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    return CartService.get_cart(token, db, cart_id)


# Create New Cart
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CartOut)
def create_cart(
        cart: CartCreate, db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    return CartService.create_cart(token, db, cart)


# Update Existing Cart
@router.put("/{cart_id}", status_code=status.HTTP_200_OK, response_model=CartOut)
def update_cart(
        cart_id: int,
        updated_cart: CartUpdate,
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    return CartService.update_cart(token, db, cart_id, updated_cart)


# Delete Cart By User ID
@router.delete("/{cart_id}", status_code=status.HTTP_200_OK, response_model=CartOutDelete)
def delete_cart(
        cart_id: int, db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    return CartService.delete_cart(token, db, cart_id)
