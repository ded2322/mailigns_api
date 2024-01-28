from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Clients(Base):
    """
    Класс создающий с помощью алембика сущность client
    """
    __tablename__ = "client"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column()
