from abc import ABC, abstractmethod
from typing import Generator, Tuple

from src.schemas.response.wallet import WalletQueryResponse


class AbstractGetWalletQueriesService(ABC):
    @abstractmethod
    async def get_wallet_queries(
        self,
        offset: int | None = None,
        limit: int | None = None,
    ) -> Tuple[Generator[WalletQueryResponse, None, None], int]: ...
