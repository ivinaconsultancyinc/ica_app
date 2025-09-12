from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DocumentBase(BaseModel):
    filename: str
    file_path: str
    related_entity: Optional[str] = None
    related_entity_id: Optional[int] = None
    uploaded_by: Optional[int] = None

class DocumentCreate(DocumentBase):
    pass

class DocumentOut(DocumentBase):
    id: int
    uploaded_at: datetime

    class Config:
        orm_mode = True


