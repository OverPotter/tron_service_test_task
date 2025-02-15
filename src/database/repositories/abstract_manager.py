from abc import ABC, abstractmethod
from inspect import Traceback
from typing import Type

from src.database.repositories.wallet_query_repository import (
    WalletQueryRepository,
)


class AbstractRepositoryManager(ABC):

    @abstractmethod
    async def commit(self) -> None: ...

    @abstractmethod
    async def rollback(self) -> None: ...

    @abstractmethod
    async def close(self) -> None: ...

    async def __aenter__(self):
        return self

    async def __aexit__(
        self, exc_type: Type[Exception], exc_val: Exception, exc_tb: Traceback
    ) -> None:
        if exc_val:
            await self.rollback()
        else:
            await self.commit()
        await self.close()

    @abstractmethod
    def get_wallet_query_repository(self) -> WalletQueryRepository: ...
