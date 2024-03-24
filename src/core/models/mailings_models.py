from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from src.database import Base


class Emailing(Base):
    __tablename__ = "emailing"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True)
