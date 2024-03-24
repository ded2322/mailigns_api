import pika
from email.message import EmailMessage
from src.config import settings


def create_templates(mailings: dict):
    """
    Создает email на основе переданных email-ов
    """

    email = EmailMessage()
    email["From"] = settings.EMAIL_SENDER
    email["To"] = mailings["email_getter"]
    email["Subject"] = mailings["subject"]
    email.set_content(
        f"""
                {mailings["text_mailing"]}
               """,
        subtype="html",
    )
    return email
