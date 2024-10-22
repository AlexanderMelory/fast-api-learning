from sqlalchemy import select, RowMapping, Sequence

from app.db import async_session_maker


class BaseDAO:
    """
    Базовый DAO
    """

    model = None

    @classmethod
    async def get_all(cls) -> Sequence[RowMapping]:
        """
        Получение всех объектов модели
        """
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
        return result.mappings().all()
