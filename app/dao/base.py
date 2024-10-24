from typing import List, Any

from sqlalchemy import select, insert

from app.db import async_session_maker


class BaseDAO:
    """
    Базовый DAO
    """

    model = None

    @classmethod
    async def get_by_id(cls, id: int) -> Any:
        """
        Получение объекта по id
        """
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_one_or_none(cls, **filter_by) -> Any:
        """
        Получение одного объекта
        """
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_all(cls, **filter_by) -> List[Any]:
        """
        Получение списка всех объектов модели
        """
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def insert(cls, **data) -> None:
        """
        Добавление объекта в таблицу
        """
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
