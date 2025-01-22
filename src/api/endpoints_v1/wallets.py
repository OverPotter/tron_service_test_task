from fastapi import APIRouter


router = APIRouter(prefix="/wallets", tags=["wallets"])


# @router.post("", response_model=WalletQueryResponse)
# def get_wallet_info(wallet: WalletInfoPayload, repository_manager: OrmRepositoryManager = Depends(
#         orm_repository_manager_factory
#     ),):
#     try:
#         account = tron.get_account(wallet.address)
#         balance = str(account.get('balance', 0) / 1e6)  # Convert to TRX
#         bandwidth = str(tron.get_account_resource(wallet.address)['freeNetLimit'])
#         energy = str(tron.get_account_resource(wallet.address)['EnergyLimit'])
#
#         query = WalletQuery(
#             address=wallet.address,
#             balance=balance,
#             bandwidth=bandwidth,
#             energy=energy
#         )
#         db.add(query)
#         db.commit()
#         db.refresh(query)
#
#         return query
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))


# @router.get("", response_model=PaginatedWalletResponse)
# def get_wallet_queries(skip: int = 0, limit: int = 10, repository_manager: OrmRepositoryManager = Depends(
#         orm_repository_manager_factory
#     ),):
#     queries = db.query(WalletQuery).offset(skip).limit(limit).all()
#     total = db.query(WalletQuery).count()
#     return PaginatedWalletResponse(data=queries, total=total)
