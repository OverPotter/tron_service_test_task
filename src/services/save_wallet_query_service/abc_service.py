from abc import ABC, abstractmethod

from src.schemas.payload.wallet import WalletQueryInfoPayload
from src.schemas.response.wallet import WalletQueryResponse


class AbstractSaveWalletQueryService(ABC):
    @abstractmethod
    async def save_wallet_query(
        self,
        wallet_info: WalletQueryInfoPayload,
    ) -> WalletQueryResponse: ...
