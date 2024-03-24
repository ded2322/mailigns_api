from typing import Annotated
from fastapi import APIRouter, Depends
from src.newsletter.dependencies import email_service
from src.core.services.newsletter import NewsletterService
from src.core.schemas.newsletters_schemas import NewslettersSchema
router = APIRouter(
    prefix="/newsletter",
    tags=["Newsletter"]
)


@router.post("/creates-starts")
async def create_start(data_letters:NewslettersSchema,
                       email_services: Annotated[NewsletterService, Depends(email_service)]):
    await email_services.start_newsletter(data_letters.subject, data_letters.text_email)

