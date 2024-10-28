from fastapi import APIRouter, HTTPException
from fastapi import Response
from starlette import status

from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.dao import UserDAO
from app.users.schemas import SUserRegister, SUserLogin

router = APIRouter(prefix='/auth', tags=['Auth & Пользователи'])


@router.post('/register')
async def register(data: SUserRegister) -> None:
    """
    Регистрация пользователя
    """
    if await UserDAO.get_one_or_none(email=data.email):
        raise HTTPException(status_code=500)
    data.password = get_password_hash(data.password)
    await UserDAO.insert(**data.model_dump())


@router.post('/login')
async def login(response: Response, data: SUserLogin) -> dict:
    """
    Аутентификация пользователя
    """
    if user := await authenticate_user(data):
        acces_token = create_access_token({'sub': user.id})
        response.set_cookie(key='booking_access_token', value=acces_token, httponly=True)
        return {'access_token': acces_token}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

