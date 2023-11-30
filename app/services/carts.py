from sqlalchemy.orm import Session
from app.models.models import Cart, CartItem
from app.schemas.carts import CartUpdate, CartBase
from app.services.products import ResponseHandler
from typing import List


class CartService:
    @staticmethod
    def get_all_carts(db: Session, page: int, limit: int, search: str = ""):
        carts = db.query(Cart).offset((page - 1) * limit).limit(limit).all()
        message = f"Page {page} with {limit} carts"
        return ResponseHandler.success(message, carts)

    @staticmethod
    def get_cart(db: Session, cart_id: int):
        cart = db.query(Cart).filter(Cart.id == cart_id).first()
        if not cart:
            ResponseHandler.not_found_error("Cart", cart_id)

        return ResponseHandler.get_single_success("cart", cart_id, cart)

    @staticmethod
    def create_cart(db: Session, cart: CartBase):
        cart_dict = cart.dict()

        cart_items_data = cart_dict.pop("cart_items", [])
        cart_items = [CartItem(**item) for item in cart_items_data]

        cart_dict.pop("id", None)
        cart_db = Cart(**cart_dict, cart_items=cart_items)

        db.add(cart_db)
        db.commit()
        db.refresh(cart_db)
        return ResponseHandler.create_success("Cart", cart_db.id, cart_db)

    @staticmethod
    def update_cart(db: Session, cart_id: int, updated_cart: CartUpdate):
        cart = db.query(Cart).filter(Cart.id == cart_id).first()
        if not cart:
            return ResponseHandler.not_found_error("Cart", cart_id)

        print("cart before update :", cart)

        cart.items = [CartItem(**item.model_dump()) for item in updated_cart.items]
        db.commit()
        db.refresh(cart)
        return ResponseHandler.update_success("cart", cart.id, cart)

    @staticmethod
    def delete_cart(db: Session, cart_id: int):
        cart = db.query(Cart).filter(Cart.id == cart_id).first()
        if not cart:
            ResponseHandler.not_found_error("Cart", cart_id)

        for cart_item in cart.cart_items:
            db.delete(cart_item)

        db.delete(cart)
        db.commit()
        return ResponseHandler.delete_success("Cart", cart_id, cart)
