from sqlalchemy.ext.asyncio import AsyncSession

from src.database.repositories.abstract_manager import AbstractRepositoryManager
from src.database.repositories.wallet_query_repository import (
    WalletQueryRepository,
)
from src.db_manager import session_factory


class OrmRepositoryManager(AbstractRepositoryManager):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()

    async def close(self) -> None:
        await self._session.close()

    def get_wallet_query_repository(self) -> WalletQueryRepository:
        return WalletQueryRepository(session=self._session)


def orm_repository_manager_factory() -> OrmRepositoryManager:
    return OrmRepositoryManager(session_factory())
