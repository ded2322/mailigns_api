import sentry_sdk
from fastapi import HTTPException
from src.core.utils.repository import AbstractRepository
from src.core.schemas.mailings_schemas import EmailingSchema


class EmailingService:

    def __init__(self, user_repo: AbstractRepository):
        self.user_repo: AbstractRepository = user_repo()

    async def show_all_email(self):
        result = await self.user_repo.show_table()
        return result[0]

    async def add_email(self, user_email: EmailingSchema):
        try:
            if await self.user_repo.found_one_or_none(email=user_email.email):
                raise HTTPException(status_code=409, detail="Email already is occupied")
            await self.user_repo.insert_data(email=user_email.email)
        except Exception as e:
            sentry_sdk.capture_exception(e)

    async def delete_email(self, user_email: EmailingSchema):
        try:
            result = await self.user_repo.found_one_or_none(email=user_email.email)
            if not result:
                raise HTTPException(status_code=404, detail="Email not found")
            #                                алхимия отдается список словарей, мы обращаемся к первому словарю
            await self.user_repo.delete_data(id=result[0]["id"])
        except Exception as e:
            sentry_sdk.capture_exception(e)