from datetime import datetime
from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.schemas.mailings_schemas import SMailings, STemplatesMailings
from app.dao.mailings_dao import MailingsDao
from app.dao.clients_dao import ClientsDao


from app.tasks.tasks import send_email


router = APIRouter(prefix="/mailings", tags=["Рассылка"])


@router.get("/all")
@cache(expire=30)
async def show_mailings():
    """
    Показывает все созданные рассылки
    """
    result = await MailingsDao.show_data_table()
    return result


@router.post("/create_queue_mailings")
async def create_queue_mailings(data_email: STemplatesMailings):
    """
    Создает очередь в брокере сообщений
    """
    email = await ClientsDao().show_clients_email()
    for column in range(len(email)):
        mailings_dict = {
            "subject": data_email.subject,
            "text_mailing": data_email.text_message,
            "email_getter": email[column]["email"],
        }

        send_email.apply_async(args=[mailings_dict], eta=data_email.scheduled_date)

        await MailingsDao.insert_data(
            email_client=email[column]["email"],
            subject_mailing=data_email.subject,
            date=data_email.scheduled_date,
        )
    return {"message": "очередь успешно создана"}


@router.post("/create_and_start_mailings")
async def add_start_mailing(data_email: SMailings):
    """
    Позволяет создать рассылку и сразу ее начать
    """
    email = await ClientsDao().show_clients_email()
    for column in range(len(email)):
        mailings_dict = {
            "subject": data_email.subject,
            "text_mailing": data_email.text_message,
            "email_getter": email[column]["email"],
        }

        send_email.delay(mailings_dict)
        await MailingsDao.insert_data(
            email_client=email[column]["email"],
            subject_mailing=data_email.subject,
            date=str(datetime.now()),
        )

    return {"message": "рассылка началась"}
