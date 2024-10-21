from sqlalchemy import select

from app.db import async_session_maker


class BaseDAO:
    """
    Базовый DAO
    """

    model = None

    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
        return result.mappings().all()
