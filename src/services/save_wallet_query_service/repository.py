from src.database.repositories.wallet_query_repository import (
    WalletQueryRepository,
)
from src.schemas.payload.wallet import WalletQueryInfoPayload
from src.schemas.response.wallet import WalletQueryResponse
from src.services.save_wallet_query_service.abc_service import (
    AbstractSaveWalletQueryService,
)


class RepositorySaveWalletQueryService(AbstractSaveWalletQueryService):
    def __init__(
        self,
        wallet_query_repository: WalletQueryRepository,
    ):
        self._wallet_query_repository = wallet_query_repository

    async def save_wallet_query(
        self,
        wallet_info: WalletQueryInfoPayload,
    ) -> WalletQueryResponse:
        created_wallet_query = await self._wallet_query_repository.create(
            **wallet_info.dict()
        )

        return WalletQueryResponse.model_validate(created_wallet_query)
