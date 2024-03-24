from src.core.repositories.mailings import EmailingRepository
from src.core.services.mailings import EmailingService


def email_service():
    return EmailingService(EmailingRepository)
