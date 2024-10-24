from fastapi import APIRouter, HTTPException

from app.users.auth import get_password_hash
from app.users.dao import UserDAO
from app.users.schemas import SUserRegister


router = APIRouter(prefix='/auth', tags=['Auth & Пользователи'])


@router.post('/register')
async def register(user_data: SUserRegister):
    """
    Регистрация пользователя
    """
    if await UserDAO.get_one_or_none(email=user_data.email):
        raise HTTPException(status_code=500)
    user_data.password = get_password_hash(user_data.password)
    await UserDAO.insert(**user_data.model_dump())
