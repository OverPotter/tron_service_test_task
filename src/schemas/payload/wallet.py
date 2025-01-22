from src.schemas.payload.base import BasePayload


class WalletAddressPayload(BasePayload):
    address: str


class WalletQueryInfoPayload(BasePayload):
    address: str
    balance: str
    bandwidth: str
    energy: str
