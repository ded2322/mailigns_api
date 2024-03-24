from src.core.repositories.mailings import EmailingRepository
from src.core.services.newsletter import NewsletterService


def email_service():
    return NewsletterService(EmailingRepository)