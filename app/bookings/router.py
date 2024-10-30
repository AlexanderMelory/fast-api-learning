from datetime import date
from pprint import pprint
from typing import List

from fastapi import APIRouter, Request
from fastapi.params import Depends

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.users.depends import get_current_user
from app.users.models import User

router = APIRouter(prefix='/bookings', tags=['Бронирования'])


@router.get('')
async def get_bookings(request: Request, user: User=Depends(get_current_user)): #-> List[SBooking]:
    """
    Список бронирований
    """
    return await BookingDAO.get_all(user_id=user.id)


@router.post('')
async def add_booking(room_id: int, date_from: date, date_to: date, user_id: User = Depends(get_current_user)):
    await BookingDAO.insert(user_id, room_id, date_from, date_to)
