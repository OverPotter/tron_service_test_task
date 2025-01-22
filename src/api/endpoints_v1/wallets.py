from fastapi import APIRouter, Depends

from src.database.repositories.manager import (
    OrmRepositoryManager,
    orm_repository_manager_factory,
)
from src.schemas.payload.wallet import (
    WalletAddressPayload,
)
from src.schemas.response.wallet import WalletQueryResponse
from src.services.get_wallet_info_service.abc import (
    AbstractGetWalletInfoService,
)
from src.services.get_wallet_info_service.tron import TronGetWalletInfoService
from src.services.logging_service.logging_service import logger_factory
from src.services.save_wallet_query_service.abc import (
    AbstractSaveWalletQueryService,
)
from src.services.save_wallet_query_service.repository import (
    RepositorySaveWalletQueryService,
)
from src.services.tron_service.tron_service import tron_factory

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
    # todo: create facade to save SRP
    tron_service: AbstractGetWalletInfoService = TronGetWalletInfoService(
        tron_manger=tron, logger=logger
    )
    wallet_query_info_payload = tron_service.get_wallet_info(
        wallet_address=payload.address
    )

    async with repository_manager:
        wallet_service: AbstractSaveWalletQueryService = (
            RepositorySaveWalletQueryService(
                wallet_query_repository=repository_manager.get_wallet_query_repository(),
                logger=logger,
            )
        )
        wallet_info_response = await wallet_service.save_wallet_query(
            wallet_info=wallet_query_info_payload
        )
        return wallet_info_response


# @router.get("", response_model=PaginatedWalletQueriesResponse)
# def get_wallet_queries(skip: int = 0, limit: int = 10, repository_manager: OrmRepositoryManager = Depends(
#         orm_repository_manager_factory
#     ),):
#     queries = db.query(WalletQueryModel).offset(skip).limit(limit).all()
#     total = db.query(WalletQueryModel).count()
#     return PaginatedWalletQueriesResponse(data=queries, total=total)
