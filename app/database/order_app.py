from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

# DEPENDENCY
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


#@router.post("/api/orders/create", response_model = schemas.Order)
def create_order(order: schemas.OrderCreate):
	db = SessionLocal()
	db_order = crud.get_order(db, order_id = order.order_id)
	if db_order:
		raise HTTPException(status_code = 400, detail = "Order already exist")
	result = crud.create_order(db = db, order = order)
	db.close()
	return result


#@router.post("/api/orders/confirm", response_model = schemas.Order)
def confirm_order(order: schemas.OrderConfirm):
	db = SessionLocal()
	db_order = crud.get_order(db, order_id = order.order_id)
	if db_order:
		result = crud.confirm_order(db = db, order = order)
		db.close()
		return result
	else:
		raise HTTPException(status_code=404, detail="Order not found")

@router.get("/api/orders/list", response_model=List[schemas.Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders


#@router.get("/api/orders/item/{order_id}", response_model=schemas.Order)
def read_order(order_id: int):
    db = SessionLocal()
    db_order = crud.get_order(db, order_id = order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    db.close()
    return db_order
