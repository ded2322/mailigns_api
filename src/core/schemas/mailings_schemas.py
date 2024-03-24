from pydantic import BaseModel, EmailStr


class EmailingSchema(BaseModel):
    email: EmailStr
