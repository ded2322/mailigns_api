from sqlalchemy import select

from app.dao.base import BaseDao
from app.models.clients_models import Clients
from app.database import async_session_maker


class ClientsDao(BaseDao):
    model = Clients

    @classmethod
    async def update_email(cls, id_worker, new_email):
        """
        Обновление емейла пользователя
        """
        async with async_session_maker() as session:
            query = await session.get(cls.model, id_worker)
            query.email = new_email
            await session.commit()

    @classmethod
    async def show_clients_email(cls):
        """
        Декоратор который выдергивает из базы данных только emails
        """
        async with async_session_maker() as session:
            query = select(cls.model.email)
            result = await session.execute(query)
            return result.mappings().all()
