from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.config import settings

# Импорт пути до базы данных
engine = create_async_engine(settings.DATABASE_URL)

# Создание асинхронной сесси
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)


#
class Base(DeclarativeBase):
    pass
