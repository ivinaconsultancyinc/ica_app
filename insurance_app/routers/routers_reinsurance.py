from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from insurance_app.database import get_db
from insurance_app.schemas.reinsurance_schema import ReinsuranceContractCreate, ReinsuranceContractResponse
from insurance_app.services.reinsurance_service import create_contract, get_contracts
from typing import List

router = APIRouter(prefix="/reinsurance", tags=["Reinsurance"])

@router.post("/", response_model=ReinsuranceContractResponse)
def add_contract(contract_data: ReinsuranceContractCreate, db: Session = Depends(get_db)):
    return create_contract(db, contract_data)

@router.get("/", response_model=List[ReinsuranceContractResponse])
def list_contracts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_contracts(db, skip=skip, limit=limit)



