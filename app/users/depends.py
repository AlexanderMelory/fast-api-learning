from fastapi import HTTPException, status, Depends
from jose import jwt, JWTError
from starlette.requests import Request

from app.settings import settings
from app.users.dao import UserDAO


def get_token(request: Request):
    if token := request.cookies.get('booking_access_token'):
        return token
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, key=settings.SECRET_KEY, algorithms=[settings.SIGN_ALGORITHM])
        user = await UserDAO.get_by_id(int(payload.get('id')))
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return user
    except JWTError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
