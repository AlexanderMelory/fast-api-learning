from sqlalchemy import select, and_, or_, func, insert

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
            async with session.begin():
                user_id = int(user_id) if isinstance(user_id, str) else user_id
                room_id = int(room_id) if isinstance(room_id, str) else room_id
                booked_rooms = (
                    select(Booking.room_id).where(
                        and_(
                            Booking.room_id == room_id,
                            or_(and_(Booking.date_from < date_to, Booking.date_to > date_from)),
                        )
                    )
                ).cte('booked_rooms')
                get_rooms_left = (
                    select(Room.quantity - func.coalesce(func.count(booked_rooms.c.room_id), 0).label('rooms_left'))
                    .select_from(Room)
                    .outerjoin(booked_rooms, and_(booked_rooms.c.room_id == Room.id))
                    .where(Room.id == room_id)
                    .group_by(Room.id, Room.quantity)
                )
                rooms_left_result = await session.execute(get_rooms_left)
                rooms_left = rooms_left_result.scalar()

                if rooms_left is None or rooms_left <= 0:
                    return None
                get_price = select(Room.price).where(Room.id == room_id)
                price_result = await session.execute(get_price)
                price = price_result.scalar()
                add_new_booking = (
                    insert(Booking)
                    .values(room_id=room_id, date_from=date_from, date_to=date_to, user_id=user_id, price=price)
                    .returning(Booking)
                )
                return await session.execute(add_new_booking)
