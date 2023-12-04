from fastapi import APIRouter, Depends, Query, status
from app.db.database import get_db
from app.services.carts import CartService
from sqlalchemy.orm import Session
from app.schemas.carts import CartCreate, CartUpdate, CartOut, CartOutDelete, CartsOutList, CartsUserOutList
from app.core.security import get_current_user

router = APIRouter(tags=["Carts"], prefix="/carts")


# Get All Carts
@router.get("/", status_code=status.HTTP_200_OK, response_model=CartsOutList)
def get_all_carts(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Items per page"),
    current_user: dict = Depends(get_current_user),
):
    return CartService.get_all_carts(current_user, db, page, limit)


# Get All Carts for user
@router.get("/user/{user_id}", status_code=status.HTTP_200_OK, response_model=CartsUserOutList)
def get_all_user_carts(
    user_id: int,
    db: Session = Depends(get_db),
):
    return CartService.get_all_user_carts(db, user_id)


# Get Cart By User ID
@router.get("/{cart_id}", status_code=status.HTTP_200_OK, response_model=CartOut)
def get_cart(cart_id: int, db: Session = Depends(get_db)):
    return CartService.get_cart(db, cart_id)


# Create New Cart
@router.post("/user/", status_code=status.HTTP_201_CREATED, response_model=CartOut)
def create_cart(cart: CartCreate, db: Session = Depends(get_db)):
    return CartService.create_cart(db, cart)


# Update Existing Cart
@router.put("/{cart_id}", status_code=status.HTTP_200_OK, response_model=CartOut)
def update_cart(cart_id: int, updated_cart: CartUpdate, db: Session = Depends(get_db)):
    return CartService.update_cart(db, cart_id, updated_cart)


# Delete Cart By User ID
@router.delete("/{cart_id}", status_code=status.HTTP_200_OK, response_model=CartOutDelete)
def delete_cart(cart_id: int, db: Session = Depends(get_db)):
    return CartService.delete_cart(db, cart_id)
