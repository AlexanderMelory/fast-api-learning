from decimal import Decimal
from typing import Dict

from pydantic import BaseModel


class HotelInfo(BaseModel):
    """
    Информация об отеле
    """

    name: str
    location: str
    services: Dict[str, str]
    rooms_qty: int
    image_id: int

    class Config:
        from_attributes = True


class RoomInfo(BaseModel):
    """
    Информация о номере
    """

    hotel_id: int
    name: str
    description: str
    price: Decimal
    services: Dict[str, str]
    quantity: int
    number: int

    class Config:
        from_attributes = True
