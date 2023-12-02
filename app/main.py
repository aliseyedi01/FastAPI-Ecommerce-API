from app.routers import products, categories, carts, users
from fastapi import FastAPI
app = FastAPI()

app.include_router(products.router)
app.include_router(categories.router)
app.include_router(carts.router)
app.include_router(users.router)
