import functools
from app.db import async_session_maker


def async_session(func):
    """
    Оборачивает передаваемый метод в асинхронный контекстный менеджер сессии
    """
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        async with async_session_maker() as session:
            return await func(session=session, *args, **kwargs)

    return wrapper
