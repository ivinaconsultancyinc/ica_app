from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from typing import List

import uuid

 

from insurance_app.schemas.user_schema import UserCreate, UserUpdate, UserResponse

from insurance_app.services.user_service import UserService

from insurance_app.database import get_db  # <-- Import get_db from your shared database.py

 

router = APIRouter()

 

@router.post("/", response_model=UserResponse)

def create_user(user: UserCreate, db: Session = Depends(get_db)):

    service = UserService(db)

    return service.create_user(user)

 

@router.get("/", response_model=List[UserResponse])

def list_users(db: Session = Depends(get_db)):

    service = UserService(db)

    return service.get_all_users()

 

@router.get("/{user_id}", response_model=UserResponse)

def get_user(user_id: uuid.UUID, db: Session = Depends(get_db)):

    service = UserService(db)

    user = service.get_user_by_id(user_id)

    if not user:

        raise HTTPException(status_code=404, detail="User not found")

    return user

 

@router.put("/{user_id}", response_model=UserResponse)

def update_user(user_id: uuid.UUID, user_data: UserUpdate, db: Session = Depends(get_db)):

    service = UserService(db)

    return service.update_user(user_id, user_data)

 

@router.delete("/{user_id}")

def delete_user(user_id: uuid.UUID, db: Session = Depends(get_db)):

    service = UserService(db)

    service.delete_user(user_id)

    return {"message": "User deleted successfully"}

 
