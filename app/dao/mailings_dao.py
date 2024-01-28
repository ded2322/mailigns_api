from app.dao.base import BaseDao
from app.models.mailing_models import Mailings


class MailingsDao(BaseDao):
    model = Mailings
