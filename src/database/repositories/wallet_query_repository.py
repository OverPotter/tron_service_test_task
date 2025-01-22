from typing import Sequence

from sqlalchemy import select

from src.database.models import WalletQueryModel
from src.database.repositories.absctract_repository import AbstractRepository


class WalletQueryRepository(AbstractRepository[WalletQueryModel]):
    _model = WalletQueryModel

    async def search(
        self,
        limit: int | None = None,
        offset: int | None = None,
    ) -> tuple[Sequence[WalletQueryModel], int]:
        query = select(WalletQueryModel)

        query, total = await self._paginate(query, limit=limit, offset=offset)
        result = await self._session.execute(query)

        return result.scalars().all(), total
