from fastapi import UploadFile, APIRouter
import shutil


router = APIRouter(prefix='/images', tags=['Изображения'])


@router.post('/hotels')
async def add_hotel_image(file: UploadFile, name: int):
    """
    Добавление изображения отеля
    """
    with open(f'app/static/images/{name}.jpg', 'wb+') as f:
        f.write(await file.read())
