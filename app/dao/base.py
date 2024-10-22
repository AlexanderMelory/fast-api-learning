from sqlalchemy import select
from app.utils.decorators import async_session


class BaseDAO:
    """
    Базовый DAO
    """

    model = None

    @classmethod
    @async_session
    async def get_all(cls, session):
        query = select(cls.model)
        result = await session.execute(query)
        return result.mappings().all()
