from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from insurance_app import models
from insurance_app.schemas.customer_schema import CustomerCreate, CustomerUpdate, CustomerOut
from insurance_app.database import get_db
from insurance_app.services import customer_service
router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)
@router.post("/", response_model=CustomerOut, status_code=status.HTTP_201_CREATED)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return customer_service.create_customer(db, customer)
@router.get("/", response_model=List[CustomerOut])
def get_all_customers(db: Session = Depends(get_db)):
    return customer_service.get_all_customers(db)
@router.get("/{customer_id}", response_model=CustomerOut)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    return customer_service.get_customer_by_id(db, customer_id)
@router.put("/{customer_id}", response_model=CustomerOut)
def update_customer(customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    return customer_service.update_customer(db, customer_id, customer)
@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer_service.delete_customer(db, customer_id)
    return None




