from sqlalchemy import delete, insert, select
from sqlalchemy.exc import SQLAlchemyError

from app.database import async_session_maker


class BaseDao:
    model = None

    @classmethod
    async def show_data_table(cls):
        """
        Показывает все записи в таблице
        """
        try:
            async with async_session_maker() as session:
                query = select(cls.model)
                result = await session.execute(query)
                return result.mappings().all()

        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                # возбуждать ошибку
                msg = "Database Exc:"
                print(f"{str(e)}")
            else:
                msg = "Unknown Exc"
                print(f"{str(e)}")
            return None

    @classmethod
    async def insert_data(cls, **kwargs):
        """
        Добавляет данные в базу данных
        """
        try:
            async with async_session_maker() as session:
                query = insert(cls.model).values(**kwargs)
                await session.execute(query)
                await session.commit()
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                # возбуждать ошибку
                msg = "Database Exc:"
                print(f"{str(e)}")
            else:
                msg = "Unknown Exc"
                print(f"{str(e)}")
            return None

    @classmethod
    async def found_one(cls, **kwargs):
        """
        Ищет запись в базе данных
        """
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def delete_date(cls, **kwargs):
        """
        Удаляет данные из таблицы
        """
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**kwargs)
            await session.execute(query)
            await session.commit()
