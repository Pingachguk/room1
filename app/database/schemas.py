from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Order(BaseModel):
	order_id: str
	action: str
	club_id: Optional[str] = None
	utoken: Optional[str] = None
	phone: Optional[str] = None
	confirm: Optional[bool]
	type: Optional[str] = None
	ticket_id: Optional[str] = None
	appointment_id: Optional[str] = None
	promocode: Optional[str] = None
	created_at: Optional[datetime] = None
	updated_at: Optional[datetime] = None

	class Config:
		orm_mode = True

class OrderCreate(BaseModel):
	order_id: str
	action: str
	club_id: Optional[str] = None
	phone: Optional[str] = None
	utoken: Optional[str] = None
	type: Optional[str] = None
	ticket_id: Optional[str] = None
	appointment_id: Optional[str] = None
	promocode: Optional[str] = None

	class Config:
		orm_mode = True

class OrderConfirm(BaseModel):
	order_id: str
	confirm: bool

	class Config:
		orm_mode = True

