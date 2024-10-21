from app.bookings.models import Booking
from app.dao.base import BaseDAO


class BookingDAO(BaseDAO):
    """
    DAO для бронирований
    """

    model = Booking
