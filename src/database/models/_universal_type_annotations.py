import datetime
from typing import Annotated

from sqlalchemy import func
from sqlalchemy.orm import mapped_column

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
created_at = Annotated[
    datetime.datetime, mapped_column(server_default=func.now())
]
