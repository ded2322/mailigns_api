import smtplib
import logging
import sentry_sdk
from src.config import settings


def send_email(templates):
    """
    Отправляет email и логирует результат.
    """
    try:
        with smtplib.SMTP_SSL(host=settings.HOST_SMTP, port=settings.PORT_SMTP) as smtp:
            smtp.login(settings.EMAIL_SENDER, settings.PASSWORD)
            response = smtp.send_message(templates)
            if response:
                logging.info(f"SMTP Response: {response}")

            else:
                logging.info("Сообщение успешно отправлено")
    except Exception as e:
        sentry_sdk.capture_exception(e)
