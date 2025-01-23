from src.schemas.response.wallet import WalletQueryResponse
from src.services.create_wallet_query_service.abc_service import (
    AbstractCreateWalletQueryService,
)
from src.services.get_wallet_info_service.abc_service import (
    AbstractGetWalletInfoService,
)
from src.services.logging_service.logging_factory import Logger
from src.services.save_wallet_query_service.abc_service import (
    AbstractSaveWalletQueryService,
)


class FacadeCreateWalletQueryService(AbstractCreateWalletQueryService):
    def __init__(
        self,
        get_wallet_ifo_service: AbstractGetWalletInfoService,
        save_wallet_query_service: AbstractSaveWalletQueryService,
        logger: Logger,
    ):
        self._get_wallet_ifo_service = get_wallet_ifo_service
        self._save_wallet_query_service = save_wallet_query_service
        self._logger = logger

    async def create_wallet_query(
        self, wallet_address: str
    ) -> WalletQueryResponse:
        wallet_query_info_payload = (
            self._get_wallet_ifo_service.get_wallet_info(
                wallet_address=wallet_address
            )
        )
        self._logger.info(f"Get wallet info: {wallet_query_info_payload}.")

        wallet_info_response = (
            await self._save_wallet_query_service.save_wallet_query(
                wallet_info=wallet_query_info_payload
            )
        )
        self._logger.info(
            f"Wallet info with address {wallet_info_response.address} saved in database successfully."
        )

        return wallet_info_response
