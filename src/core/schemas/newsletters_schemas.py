from pydantic import BaseModel


class NewslettersSchema(BaseModel):
    subject:str
    text_email:str
