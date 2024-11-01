from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.bookings.router import router as booking_router
from app.hotels.router import router as hotel_router
from app.pages.router import router as page_router
from app.users.router import router as user_router
from app.images.router import router as image_router

app = FastAPI()


app.mount('/static', StaticFiles(directory='app/static'), name='static')
app.include_router(page_router)
app.include_router(user_router)
app.include_router(booking_router)
app.include_router(hotel_router)
app.include_router(image_router)
