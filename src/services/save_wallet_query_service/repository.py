from ...database.repositories.wallet_query_repository import (
    WalletQueryRepository,
)
from ...schemas.payload.wallet import WalletQueryInfoPayload
from ...schemas.response.wallet import WalletQueryResponse
from ..logging_service.logging_service import Logger
from .abc import AbstractSaveWalletQueryService


class RepositorySaveWalletQueryService(AbstractSaveWalletQueryService):
    def __init__(
        self, wallet_query_repository: WalletQueryRepository, logger: Logger
    ):
        self._wallet_query_repository = wallet_query_repository
        self._logger = logger

    async def save_wallet_query(
        self,
        wallet_info: WalletQueryInfoPayload,
    ) -> WalletQueryResponse:
        print(wallet_info.dict())
        created_wallet_query = await self._wallet_query_repository.create(
            **wallet_info.dict()
        )
        self._logger.info(
            f"Wallet info with address {wallet_info.address} saved in database successfully."
        )
        return WalletQueryResponse.model_validate(created_wallet_query)
