from abc import ABC, abstractmethod

from src.schemas.response.wallet import WalletQueryResponse


class AbstractCreateWalletQueryService(ABC):
    @abstractmethod
    def create_wallet_query(
        self, wallet_address: str
    ) -> WalletQueryResponse: ...
