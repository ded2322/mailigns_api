import sentry_sdk
from src.core.utils.repository import AbstractRepository
from src.database import async_session_maker
from sqlalchemy import select, insert, delete


class SqlAlchemyRepository(AbstractRepository):
    model = None

    @classmethod
    async def show_table(cls):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def found_one_or_none(cls, **kwargs):
        async with async_session_maker() as session:
            try:
                query = select(cls.model).filter_by(**kwargs)
                result = await session.execute(query)
                return result.mappings().one_or_none()
            except Exception as e:
                sentry_sdk.capture_exception(e)

    @classmethod
    async def insert_data(cls, **kwargs):
        async with async_session_maker() as session:
            try:
                query = insert(cls.model).values(**kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                sentry_sdk.capture_exception(e)

    @classmethod
    async def delete_data(cls, **kwargs):
        async with async_session_maker() as session:
            try:
                query = delete(cls.model).filter_by(**kwargs)
                await session.execute(query)
                await session.commit()
            except Exception as e:
                sentry_sdk.capture_exception(e)
