from sqlalchemy.orm import Mapped

from src.database.models._universal_type_annotations import created_at, intpk
from src.database.models.base import Base


class WalletQueryModel(Base):
    __tablename__ = "wallet_queries"

    id: Mapped[intpk]
    address: Mapped[str]
    balance: Mapped[str]
    bandwidth: Mapped[str]
    energy: Mapped[str]
    created_at: Mapped[created_at]
