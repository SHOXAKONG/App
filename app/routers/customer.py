from datetime import timedelta
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, auth
from app.database import get_db
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()


@router.get("/products", response_model=List[schemas.Product])
def list_products(db: Session = Depends(get_db)):
    return crud.get_products(db)


@router.post("/orders", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)


@router.get("/orders/{customer_id}", response_model=List[schemas.Order])
def get_customer_orders(customer_id: int, db: Session = Depends(get_db)):
    return crud.get_orders_by_customer(db, customer_id=customer_id)


@router.get("/orders/{order_id}/status")
def get_order_status(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order_by_id(db, id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"status": db_order.status}


