from sqlalchemy import Column, String, Enum, DateTime

from sqlalchemy.dialects.postgresql import UUID

from insurance_app.database import Base

import uuid

import datetime

 

class User(Base):

    __tablename__ = "users"

    __table_args__ = {'extend_existing': True}

 

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)

    username = Column(String, unique=True, nullable=False, index=True)

    password_hash = Column(String, nullable=False)

    role = Column(Enum("admin", "manager", "agent", "customer", name="user_role_enum"), nullable=False)

    email = Column(String, unique=True, nullable=False)

    status = Column(Enum("Active", "Inactive", "Blocked", name="user_status_enum"), default="Active")

    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
