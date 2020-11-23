from sqlalchemy.orm import Session
from . import models, schemas

def get_order(db: Session, order_id: str):
	return db.query(models.Order).filter(models.Order.order_id == order_id).first()

def get_orders(db: Session, skip: int = 0, limit: int = 100):
	return db.query(models.Order).offset(skip).limit(limit).all()

def create_order(db: Session, order: schemas.OrderCreate):
	db_order = models.Order(**order.dict())
	db.add(db_order)
	db.commit()
	db.refresh(db_order)
	return db_order

def confirm_order(db: Session, order: schemas.OrderConfirm):
	order_query = db.query(models.Order).filter(models.Order.order_id == order.order_id).first()
	order_query.confirm = order.confirm
	db.commit()
	return order_query


