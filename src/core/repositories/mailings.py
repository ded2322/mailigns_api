from src.core.utils.slqalchemy_repository import SqlAlchemyRepository
from src.core.models.mailings_models import Emailing


class EmailingRepository(SqlAlchemyRepository):
    model = Emailing
