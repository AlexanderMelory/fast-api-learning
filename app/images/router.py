from fastapi import UploadFile, APIRouter
import aiofiles
from app.settings import settings
from app.tasks.tasks import process_image

router = APIRouter(prefix='/images', tags=['Изображения'])


@router.post('/hotels')
async def add_hotel_image(file: UploadFile, name: int):
    """
    Добавление изображения отеля
    """
    image_path = f'{settings.IMAGES_DIR}/{name}.jpg'
    async with aiofiles.open(image_path, 'wb+') as f:
        await f.write(await file.read())
        process_image.delay(image_path)
