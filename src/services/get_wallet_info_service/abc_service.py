from abc import ABC, abstractmethod

from src.schemas.payload.wallet import WalletQueryInfoPayload


class AbstractGetWalletInfoService(ABC):
    @abstractmethod
    def get_wallet_info(
        self, wallet_address: str
    ) -> WalletQueryInfoPayload: ...
