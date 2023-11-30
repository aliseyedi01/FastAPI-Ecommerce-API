from sqlalchemy.orm import Session
from app.models.models import Cart, CartItem, Product
from app.schemas.carts import CartUpdate, CartBase, CartCreate
from app.services.products import ResponseHandler
from typing import List


class CartService:
    @staticmethod
    def get_all_carts(db: Session, page: int, limit: int, search: str = ""):
        carts = db.query(Cart).offset((page - 1) * limit).limit(limit).all()
        message = f"Page {page} with {limit} carts"
        return ResponseHandler.success(message, carts)

    @staticmethod
    def get_all_user_carts(db: Session, user_id: int):
        carts = db.query(Cart).filter(Cart.user_id == user_id).all()
        message = f"All carts for user with ID {user_id}"
        return ResponseHandler.success(message, carts)

    @staticmethod
    def get_cart(db: Session, cart_id: int):
        cart = db.query(Cart).filter(Cart.id == cart_id).first()
        if not cart:
            ResponseHandler.not_found_error("Cart", cart_id)

        return ResponseHandler.get_single_success("cart", cart_id, cart)

    @staticmethod
    def create_cart(db: Session, cart: CartCreate):
        cart_dict = cart.dict()

        cart_dict.pop("id", None)

        cart_items_data = cart_dict.pop("cart_items", [])
        cart_items = []
        total_amount = 0
        for item_data in cart_items_data:
            product_id = item_data['product_id']
            quantity = item_data['quantity']

            product = db.query(Product).filter(Product.id == product_id).first()
            if not product:
                return ResponseHandler.not_found_error("Product", product_id)

            subtotal = quantity * product.price
            cart_item = CartItem(product_id=product_id, quantity=quantity, subtotal=subtotal)
            total_amount += subtotal

            cart_items.append(cart_item)
        cart_db = Cart(cart_items=cart_items, total_amount=total_amount, **cart_dict)

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
