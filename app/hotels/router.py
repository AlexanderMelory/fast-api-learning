from datetime import date
from typing import List

from fastapi import APIRouter
from fastapi.params import Query
from fastapi_cache.decorator import cache

from app.hotels.dao import HotelDAO, RoomDAO
from app.hotels.schemas import HotelInfo, RoomInfo

router = APIRouter(prefix='/hotels', tags=['Отели'])


@router.get('/')
@cache(expire=60)
async def get_hotels_by_location_time(location: str) -> List[HotelInfo]:
    """
    Получение отелей по локации
    """
    return await HotelDAO.get_hotel_by_filter(location=location)


@router.get('/{hotel_id}/rooms')
async def get_rooms_by_time(
    hotel_id: int, date_from: date = Query(..., description='Тест'), date_to: date = Query(..., description='Тест')
) -> List[RoomInfo]:
    """
    Получение комнат по отелю и датам
    """
    return await RoomDAO.get_room_by_filter(hotel_id=hotel_id, date_from=date_from, date_to=date_to)
