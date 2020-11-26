from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from .database import Base

class Order(Base):
	__tablename__ = "orders"

	id = Column(Integer, primary_key=True, index=True)
	order_id = Column(String, unique=True, index=True)
	action = Column(String, index=True)
	confirm = Column(Boolean, default=False)
	club_id = Column(String)
	utoken = Column(String)
	phone = Column(String)
	type = Column(String)
	ticket_id = Column(String)
	appointment_id = Column(String)
	promocode = Column(String)
	created_at = Column(DateTime(timezone=True), server_default = func.now())
	updated_at = Column(DateTime(timezone=True), onupdate = func.now())