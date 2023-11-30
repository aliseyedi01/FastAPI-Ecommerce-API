from app.routers import products, categories, carts
from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI in app directory!"}


app.include_router(products.router)
app.include_router(categories.router)
app.include_router(carts.router)
