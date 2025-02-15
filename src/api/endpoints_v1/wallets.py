from fastapi import APIRouter, Depends

from src.database.repositories.manager import (
    OrmRepositoryManager,
    orm_repository_manager_factory,
)
from src.schemas.payload.wallet import WalletAddressPayload
from src.schemas.response.base import BaseResponseWithPagination, Pagination
from src.schemas.response.wallet import WalletQueryResponse
from src.services.create_wallet_query_service.abc_service import (
    AbstractCreateWalletQueryService,
)
from src.services.create_wallet_query_service.facade import (
    FacadeCreateWalletQueryService,
)
from src.services.get_wallet_info_service.tron import TronGetWalletInfoService
from src.services.get_wallet_queries_service.abc_service import (
    AbstractGetWalletQueriesService,
)
from src.services.get_wallet_queries_service.repository import (
    RepositoryGetWalletQueriesService,
)
from src.services.logging_service.logging_factory import logger_factory
from src.services.save_wallet_query_service.repository import (
    RepositorySaveWalletQueryService,
)
from src.services.tron_service.tron_factory import tron_factory

router = APIRouter(prefix="/wallets", tags=["wallet"])

tron = tron_factory()
logger = logger_factory()


@router.post("", response_model=WalletQueryResponse)
async def get_wallet_info(
    payload: WalletAddressPayload,
    repository_manager: OrmRepositoryManager = Depends(
        orm_repository_manager_factory
    ),
):

    async with repository_manager:
        wallet_service: AbstractCreateWalletQueryService = (
            FacadeCreateWalletQueryService(
                get_wallet_ifo_service=TronGetWalletInfoService(
                    tron_manger=tron
                ),
                save_wallet_query_service=RepositorySaveWalletQueryService(
                    wallet_query_repository=repository_manager.get_wallet_query_repository(),
                ),
                logger=logger,
            )
        )

        wallet_info_response = await wallet_service.create_wallet_query(
            wallet_address=payload.address
        )
        return wallet_info_response


@router.get("", response_model=BaseResponseWithPagination[WalletQueryResponse])
async def get_wallet_queries(
    offset: int | None = None,
    limit: int | None = None,
    repository_manager: OrmRepositoryManager = Depends(
        orm_repository_manager_factory
    ),
):
    async with repository_manager:
        wallet_service: AbstractGetWalletQueriesService = (
            RepositoryGetWalletQueriesService(
                wallet_query_repository=repository_manager.get_wallet_query_repository(),
                logger=logger,
            )
        )
        entities, total = await wallet_service.get_wallet_queries(
            offset=offset,
            limit=limit,
        )

        return BaseResponseWithPagination(
            data=list(entities),
            pagination=Pagination(
                limit=limit or total, offset=offset or 0, total=total
            ),
        )
