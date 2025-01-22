from datetime import datetime
from typing import List

from src.schemas.response.base import BaseResponse


class WalletQueryResponse(BaseResponse):
    id: int
    address: str
    balance: str
    bandwidth: str
    energy: str
    created_at: datetime


class PaginatedWalletResponse(BaseResponse):
    data: List[WalletQueryResponse]
    total: int
