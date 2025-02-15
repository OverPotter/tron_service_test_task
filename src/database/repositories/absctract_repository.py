from abc import ABC
from typing import Generic, Sequence, Tuple, Type, TypeVar

from sqlalchemy import delete, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.database.models.base import Base

_MODEL_TYPE = TypeVar("_MODEL_TYPE", bound=Base)
_QUERY = TypeVar("_QUERY")


class AbstractRepository(ABC, Generic[_MODEL_TYPE]):
    _model: Type[_MODEL_TYPE] | None = None

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_all(self) -> Sequence[_MODEL_TYPE]:
        query = select(self._model)
        result = await self._session.execute(query)
        return result.scalars().all()

    async def create(self, **kwargs) -> _MODEL_TYPE:
        entity = self._model(**kwargs)
        self._session.add(entity)
        await self._session.commit()
        return entity

    async def get(self, **kwargs) -> _MODEL_TYPE:
        result = await self._session.execute(
            select(self._model).filter_by(**kwargs)
        )
        entity = result.scalars().first()
        return entity

    async def delete(self, **kwargs) -> None:
        query = delete(self._model).filter_by(**kwargs)
        await self._session.execute(query)

    async def _paginate(
        self,
        query: _QUERY,
        limit: int | None,
        offset: int | None,
        unique: bool = True,
    ) -> Tuple[_QUERY, int]:
        if unique:
            count_query = select(func.count()).select_from(
                query.distinct().subquery()
            )
        else:
            count_query = select(func.count()).select_from(query.subquery())
        if limit is not None:
            query = query.limit(limit)
        if offset is not None:
            query = query.offset(offset)

        count_result = await self._session.execute(count_query)
        return query, count_result.scalar()
