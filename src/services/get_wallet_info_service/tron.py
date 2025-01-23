from tronpy import Tron

from src.schemas.payload.wallet import WalletQueryInfoPayload
from src.services.get_wallet_info_service.abc_service import (
    AbstractGetWalletInfoService,
)


class TronGetWalletInfoService(AbstractGetWalletInfoService):
    def __init__(
        self,
        tron_manger: Tron,
    ):
        self._tron_manager = tron_manger

    def get_wallet_info(self, wallet_address: str) -> WalletQueryInfoPayload:
        account = self._tron_manager.get_account(wallet_address)
        balance = str(account.get("balance", 0) / 1e6)
        bandwidth = str(
            self._tron_manager.get_account_resource(wallet_address)[
                "freeNetLimit"
            ]
        )
        energy = str(
            self._tron_manager.get_account_resource(wallet_address)[
                "TotalEnergyLimit"
            ]
        )

        wallet_query_info_payload = WalletQueryInfoPayload(
            address=wallet_address,
            balance=balance,
            bandwidth=bandwidth,
            energy=energy,
        )
        return wallet_query_info_payload
