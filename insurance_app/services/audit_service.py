from sqlalchemy.orm import Session
from insurance_app.models.audit import AuditLog
from insurance_app.schemas.audit_schema import AuditLogCreate

def create_audit_log(db: Session, audit_data: AuditLogCreate) -> AuditLog:
    audit_log = AuditLog(**audit_data.dict())
    db.add(audit_log)
    db.commit()
    db.refresh(audit_log)
    return audit_log

def get_audit_logs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AuditLog).offset(skip).limit(limit).all()

