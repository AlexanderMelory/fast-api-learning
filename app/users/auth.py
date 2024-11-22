from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import jwt
from passlib.context import CryptContext

from app.settings import settings
from app.users.dao import UserDAO
from app.users.models import User


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password: str) -> str:
    """
    Хеширование пароля
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Верификация пароля
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    """
    Создание JWT-токена
    """
    to_encode = data.copy()
    to_encode.update({'exp': datetime.now(timezone.utc) + timedelta(minutes=15)})
    encoded_jwt = jwt.encode(to_encode, key=settings.SECRET_KEY, algorithm=settings.SIGN_ALGORITHM)
    return encoded_jwt


async def authenticate_user(data) -> Optional[User]:
    """
    Аутентификация пользователя
    """
    if (user := await UserDAO.get_one_or_none(email=data.email)) and verify_password(data.password, user.password):
        return user
    return
