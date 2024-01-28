from email.message import EmailMessage

from app.mailing.config_email import *


def create_email(mailings: dict):
    """
    Создает email на основе переданных email-ов
    """

    email = EmailMessage()
    email["From"] = EMAIL_SENDER
    email["To"] = mailings["email_getter"]
    email["Subject"] = mailings["subject"]
    email.set_content(
        f"""
                {mailings["text_mailing"]}
               """,
        subtype="html",
    )
    return email
