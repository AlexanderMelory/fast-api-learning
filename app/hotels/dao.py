from app.dao.base import BaseDAO
from app.db import async_session_maker
from app.hotels.models import Hotel, Room
from sqlalchemy import select, and_, or_, func, insert


class HotelDAO(BaseDAO):
    """
    DAO для отелей
    """

    model = Hotel

    @classmethod
    async def get_hotel_by_filter(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            hotels = await session.execute(query)
            return hotels.scalars().all()


class RoomDAO(BaseDAO):
    """
    DAO для комнат
    """

    model = Room

    @classmethod
    async def get_room_by_filter(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            rooms = await session.execute(query)
            return rooms.scalars().all()
