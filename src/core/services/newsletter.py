from src.core.utils.repository import AbstractRepository
from src.core.task_manager.email_templates import create_templates
from src.core.task_manager.tasks import send_email


class NewsletterService:
    def __init__(self, user_repo: AbstractRepository):
        self.user_repo: AbstractRepository = user_repo()

    async def start_newsletter(self, subject, text_mailing):
        result = await self.user_repo.show_table()
        for email in result:
            text_templates = {"email_getter": email["email"],
                              "subject": subject,
                              "text_mailing": text_mailing}
            ret = create_templates(text_templates)
            send_email(ret)
