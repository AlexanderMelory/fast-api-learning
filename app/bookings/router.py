from fastapi import APIRouter

from app.bookings.dao import BookingDAO


router = APIRouter(prefix='/bookings', tags=['Бронирования'])


@router.get('')
async def get_bookings():
    """
    Список бронирований
    """
    return await BookingDAO.get_all()
