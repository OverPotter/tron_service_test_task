from tronpy import Tron

from src._settings import settings_factory

settings = settings_factory()


def tron_factory() -> Tron:
    tron = Tron(network="shasta")
    tron.provider.headers = {"TRON-PRO-API-KEY": settings.TRON_API_KEY}
    return tron
