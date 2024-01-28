import smtplib
import logging

from app.tasks.celerys import celery
from app.mailing.config_email import *
from app.tasks.email_templates import create_email


@celery.task
def send_email(mailings: dict):
    """
    Отправляет email и логирует результат.
    """
    try:
        msg_content = create_email(mailings)
        with smtplib.SMTP_SSL(host=HOST_SMTP, port=PORT_SMTP) as smtp:
            smtp.login(EMAIL_SENDER, PASSWORD)
            content = msg_content

            # Отправляем сообщение и логируем ответ
            response = smtp.send_message(content)

            if response:
                logging.info(f"SMTP Response: {response}")
                return False  # Можно рассматривать как неудачу, если есть ответ сервера
            else:
                logging.info("Сообщение успешно отправлено")
                return True
    except Exception as e:
        logging.error(f"Ошибка при отправке сообщения: {str(e)}")
        return False
