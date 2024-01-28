import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


from app.database import Base


class Mailings(Base):
    """
    Класс создающий с помощью алембика сущность mailing
    """
    __tablename__ = "mailing"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email_client: Mapped[str] = mapped_column(
        ForeignKey("client.email", ondelete="CASCADE")
    )
    subject_mailing: Mapped[str]
    date: Mapped[str]
