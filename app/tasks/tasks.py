from pathlib import Path

from PIL import Image
from celery import shared_task

from app.settings import settings


@shared_task
def process_image(path: str) -> None:
    """
    Ресайз изображений и сохранение их в директорию изображений
    """
    image_path = Path(path)
    image = Image.open(image_path)
    image_resized_1000_500 = image.resize((1000, 500))
    image_resized_200_100 = image.resize((200, 100))
    image_resized_1000_500.save(f'{settings.IMAGES_DIR}/1000_500_{image_path.name}')
    image_resized_200_100.save(f'{settings.IMAGES_DIR}/200_100_{image_path.name}')
