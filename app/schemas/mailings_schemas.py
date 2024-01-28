from pydantic import BaseModel, validator
from datetime import datetime


class SMailings(BaseModel):
    # добавить возможность, заголовка и основного текста
    subject: str
    text_message: str


class STemplatesMailings(BaseModel):
    subject: str
    text_message: str
    scheduled_date: str

    @validator("scheduled_date")
    def validate_date(cls, v) -> str:
        # Для проверки формата даты
        date_format = "%d-%m-%Y %H:%M"
        try:
            # Преобразование строки в дату
            scheduled_date = datetime.strptime(v, date_format)
        except ValueError:
            raise ValueError("Формат даты должен быть DD-MM-YYYY HH:MM")

        # Проверка, что дата находится в будущем
        if scheduled_date <= datetime.now():
            raise ValueError("Date must be in the future")

        return str(scheduled_date)
