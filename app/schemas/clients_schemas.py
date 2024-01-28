from pydantic import BaseModel, EmailStr
from typing import Optional


class SClients(BaseModel):
    name: str
    email: EmailStr


class SUpdateData(BaseModel):
    id: int
    name: Optional[str]
    new_email: Optional[EmailStr]


class SDelete(BaseModel):
    id: int
