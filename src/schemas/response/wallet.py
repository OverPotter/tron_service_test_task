from datetime import datetime

from src.schemas.response.base import BaseResponse


class WalletQueryResponse(BaseResponse):
    id: int
    address: str
    balance: str
    bandwidth: str
    energy: str
    created_at: datetime
