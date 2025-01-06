from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models, schemas



def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product_by_id(db: Session, id: int):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


def update_product(db: Session, id: int, product: schemas.ProductUpdate):
    db_product = db.query(models.Product).filter(models.Product.id == id).first()
    if db_product:
        for key, value in product.dict(exclude_unset=True).items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, id: int):
    db_product = db.query(models.Product).filter(models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()

def get_orders(db: Session):
    return db.query(models.Order).all()

def get_orders_by_customer(db: Session, customer_id: int):
    return db.query(models.Order).filter(models.Order.customer_id == customer_id).all()


def get_order_by_id(db: Session, id: int):
    return db.query(models.Order).filter(models.Order.id == id).first()


def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(customer_id=order.customer_id, status="Pending")
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    for item in order.items:
        db_order_detail = models.OrderDetail(
            order_id=db_order.id,
            product_id=item.product_id,
            quantity=item.quantity
        )
        db.add(db_order_detail)
    db.commit()
    return db_order

def get_products(db: Session):
    return db.query(models.Product).all()

def get_product_by_name(db: Session, name: str):
    return db.query(models.Product).filter(models.Product.name == name).first()


def get_user_by_username(db: Session, username: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user