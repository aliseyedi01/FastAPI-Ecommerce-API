from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.models import Product
from app.schemas.products import ProductOut, ProductsOut
from typing import List, Optional
router = APIRouter(tags=["Products"], prefix="/products")


# Get All Products
@router.get("/", response_model=ProductsOut)
def get_all_products(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Items per page"),
    search: Optional[str] = "",
):
    products = db.query(Product).order_by(Product.id.asc()).filter(
        Product.title.contains(search)).limit(limit).offset((page - 1) * limit).all()
    return {"message": f"Page {page} with {limit} products", "products": products}


# Get Product By ID
@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": f"Details for product with id: {product_id}", "product": product}


# Create New Product
@router.post("/", response_model=ProductOut)
def create_product(product: dict, db: Session = Depends(get_db)):
    db_product = Product(**product)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return {"message": "Product created successfully", "product": db_product}


# Update Exist Product
@router.put("/{product_id}", response_model=ProductOut)
def update_product(product_id: int, updated_product: dict, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in updated_product.items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return {"message": f"Product {product_id} updated successfully", "product": db_product}


# Delete Product By ID
@router.delete("/{product_id}", response_model=ProductOut)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"message": f"Product {product_id} deleted successfully", "product": db_product}
