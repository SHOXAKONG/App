from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/products", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_name(db, name=product.name)
    if db_product:
        raise HTTPException(status_code=400, detail="Product already exists")
    return crud.create_product(db=db, product=product)

@router.get("/products/{id}", response_model=schemas.Product)
def read_product(id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_id(db, id=id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.put("/products/{id}", response_model=schemas.Product)
def update_product(id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_id(db, id=id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.update_product(db=db, id=id, product=product)

@router.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_id(db, id=id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    crud.delete_product(db=db, id=id)
    return {"message": "Product deleted successfully"}

@router.get("/orders", response_model=List[schemas.Order])
def list_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)

@router.get("/orders/{id}", response_model=schemas.Order)
def read_order(id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order_by_id(db, id=id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order
