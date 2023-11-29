from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.models import Product, Category
from app.schemas.products import ProductCreate


class ResponseHandler:
    @staticmethod
    def success(message, data=None):
        return {"message": message, "data": data}

    @staticmethod
    def get_single_success(name, id, data):
        message = f"Details for {name} with id {id}"
        return ResponseHandler.success(message, data)

    @staticmethod
    def create_success(name, id, data):
        message = f"{name} with id {id} created successfully"
        return ResponseHandler.success(message, data)

    @staticmethod
    def update_success(name, id, data):
        message = f"{name} with id {id} updated successfully"
        return ResponseHandler.success(message, data)

    @staticmethod
    def delete_success(name, id, data):
        message = f"{name} with id {id} deleted successfully"
        return ResponseHandler.success(message, data)

    @staticmethod
    def not_found_error(name="", id=None):
        message = f"{name} With Id {id} Not Found!"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)


class ProductService:
    @staticmethod
    def get_all_products(db: Session, page: int, limit: int, search: str = ""):
        products = db.query(Product).order_by(Product.id.asc()).filter(
            Product.title.contains(search)).limit(limit).offset((page - 1) * limit).all()
        return {"message": f"Page {page} with {limit} products", "data": products}

    @staticmethod
    def get_product(db: Session, product_id: int):
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            ResponseHandler.not_found_error("Product", product_id)
        return ResponseHandler.get_single_success(product.title, product_id, product)

    @staticmethod
    def create_product(db: Session, product: ProductCreate):
        category_exists = db.query(Category).filter(Category.id == product.category_id).first()
        if not category_exists:
            ResponseHandler.not_found_error("Category", product.category_id)

        product_dict = product.dict()
        db_product = Product(**product_dict)
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return ResponseHandler.create_success(db_product.title, db_product.id, db_product)

    @staticmethod
    def update_product(db: Session, product_id: int, updated_product: dict):
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if not db_product:
            ResponseHandler.not_found_error("Product", product_id)

        for key, value in updated_product.items():
            setattr(db_product, key, value)

        db.commit()
        db.refresh(db_product)
        return ResponseHandler.update_success(db_product.title, db_product.id, db_product)

    @staticmethod
    def delete_product(db: Session, product_id: int):
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if not db_product:
            ResponseHandler.not_found_error("Product", product_id)
        db.delete(db_product)
        db.commit()
        return ResponseHandler.delete_success(db_product.title, db_product.id, db_product)
