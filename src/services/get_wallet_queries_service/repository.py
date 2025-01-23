from typing import Generator, Tuple

from src.database.repositories.wallet_query_repository import (
    WalletQueryRepository,
)
from src.schemas.response.wallet import WalletQueryResponse
from src.services.get_wallet_queries_service.abc_service import (
    AbstractGetWalletQueriesService,
)
from src.services.logging_service.logging_factory import Logger


class RepositoryGetWalletQueriesService(AbstractGetWalletQueriesService):
    def __init__(
        self, wallet_query_repository: WalletQueryRepository, logger: Logger
    ):
        self._wallet_query_repository = wallet_query_repository
        self._logger = logger

    async def get_wallet_queries(
        self,
        offset: int | None = None,
        limit: int | None = None,
    ) -> Tuple[Generator[WalletQueryResponse, None, None], int]:
        wallet_queries, total = await self._wallet_query_repository.search(
            limit=limit, offset=offset
        )
        self._logger.info(
            f"Successfully fetched wallet queries: {total} items found. Offset: {offset}, limit {limit}."
        )

        return (
            (
                WalletQueryResponse.model_validate(wallet_query)
                for wallet_query in wallet_queries
            ),
            total,
        )
