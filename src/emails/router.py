from typing import Annotated
from fastapi import APIRouter, Depends
from src.core.services.mailings import EmailingService
from src.emails.dependencies import email_service
from src.core.schemas.mailings_schemas import EmailingSchema

router = APIRouter(
    prefix="/email",
    tags=["Email"]
)


@router.get("/all",status_code=200,summary="")
async def all_email(email_services: Annotated[EmailingService, Depends(email_service)]):
    return await email_services.show_all_email()


@router.post("/add",status_code=201,summary="")
async def add_email(data_email: EmailingSchema,
                    email_services: Annotated[EmailingService, Depends(email_service)]):
    await email_services.add_email(data_email)
    return {"message": "email succeeded saved"}


@router.delete("/delete",status_code=201,summary="")
async def delete_email(data_email: EmailingSchema,
                       email_services: Annotated[EmailingService, Depends(email_service)]):
    await email_services.delete_email(data_email)

    return {"message": "email succeeded deleted"}
