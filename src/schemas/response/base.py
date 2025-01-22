from typing import Generic, List, TypeVar

from pydantic import BaseModel


class BaseResponse(BaseModel):
    class Config:
        from_attributes = True
        alias_generator = "to_camel"


PaginationItem = TypeVar("PaginationItem")


class Pagination(BaseResponse):
    limit: int
    offset: int
    total: int


class BaseResponseWithPagination(BaseResponse, Generic[PaginationItem]):
    data: List[PaginationItem]
    pagination: Pagination
