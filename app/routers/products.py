from fastapi import APIRouter, Depends, Query, status
from app.db.database import get_db
from app.services.products import ProductService
from sqlalchemy.orm import Session
from typing import List, Optional
from app.schemas.products import ProductCreate, ProductOut, ProductsOut, ProductOutDelete, ProductUpdate

router = APIRouter(tags=["Products"], prefix="/products")


# Get All Products
@router.get("/", status_code=status.HTTP_200_OK, response_model=ProductsOut)
def get_all_products(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Items per page"),
    search: Optional[str] = "",
):
    return ProductService.get_all_products(db, page, limit, search)


# Get Product By ID
@router.get("/{product_id}", status_code=status.HTTP_200_OK, response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return ProductService.get_product(db, product_id)


# Create New Product
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return ProductService.create_product(db, product)


# Update Exist Product
@router.put("/{product_id}", status_code=status.HTTP_200_OK, response_model=ProductOut)
def update_product(product_id: int, updated_product: ProductUpdate, db: Session = Depends(get_db)):
    return ProductService.update_product(db, product_id, updated_product)


# Delete Product By ID
@router.delete("/{product_id}", status_code=status.HTTP_200_OK, response_model=ProductOutDelete)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return ProductService.delete_product(db, product_id)
