from src.database.models import WalletQueryModel
from src.database.repositories.absctract_repository import AbstractRepository


class WalletQueryRepository(AbstractRepository[WalletQueryModel]):
    _model = WalletQueryModel
