from src.schemas.payload.base import BasePayload


class WalletInfoPayload(BasePayload):
    address: str
