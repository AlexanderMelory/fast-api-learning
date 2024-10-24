from datetime import date
from typing import Optional

from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel

from app.bookings.schemas import SBooking
from app.users.router import router as user_router
from app.bookings.router import router as booking_router


app = FastAPI()


app.include_router(user_router)
app.include_router(booking_router)


class HotelsSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


@app.get('/hotels')
def get_hotels(search_args: HotelsSearchArgs = Depends()):
    return search_args


@app.post('/bookings')
def add_booking(booking: SBooking):
    pass
