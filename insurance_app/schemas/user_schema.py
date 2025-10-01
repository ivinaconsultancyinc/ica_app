from pydantic import BaseModel, EmailStr

from typing import Optional

import uuid

 

class UserBase(BaseModel):

    username: str

    email: EmailStr

    role: str  # e.g., "admin", "manager", "agent", "customer"

    status: Optional[str] = "Active"

 

class UserCreate(UserBase):

    password: str  # Plain password for creation

 

class UserUpdate(UserBase):

    password: Optional[str] = None  # Optional for updates

 

class UserResponse(UserBase):

    id: uuid.UUID

 

    class Config:

        from_attributes = True
