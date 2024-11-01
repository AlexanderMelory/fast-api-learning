from fastapi import FastAPI

from app.bookings.router import router as booking_router
from app.hotels.router import router as hotel_router
from app.pages.router import router as page_router
from app.users.router import router as user_router

app = FastAPI()


app.include_router(page_router)
app.include_router(user_router)
app.include_router(booking_router)
app.include_router(hotel_router)
