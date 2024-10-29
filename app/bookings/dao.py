from sqlalchemy import select, and_, or_, func

from app.bookings.models import Booking
from app.dao.base import BaseDAO
from app.db import async_session_maker
from app.hotels.models import Room


class BookingDAO(BaseDAO):
    """
    DAO для бронирований
    """

    model = Booking

    @classmethod
    async def insert(cls, user_id, room_id, date_from, date_to):
        async with async_session_maker() as session:
            booked_rooms = (
                select(Booking)
                .where(
                    and_(
                        Booking.room_id == room_id,
                        or_(and_(Booking.date_from >= date_from, Booking.date_to <= date_to)),
                    )
                )

            ).cte('booked_rooms')
            rooms_left = (
                (
                    select(Room.quantity - func.count(booked_rooms.c.room_id))
                    .label('rooms_left')
                    .select_from(Room)
                    .join(booked_rooms, booked_rooms.c.room_id == Room.id)
                )
                .where(Room.id == room_id)
                .group_by(Room.quantity, booked_rooms.c.room_id)
            )
            rooms_left = await session.execute(rooms_left)
