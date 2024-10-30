from fastapi import HTTPException, status, Depends
from jose import jwt, JWTError
from starlette.requests import Request

from app import settings


def get_token(request: Request):
    if token := request.cookies.get('booking_access_token'):
        return token
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, key=settings.SECRET_KEY, algorithms=[settings.SIGN_ALGORITHM], options={"verify_exp": False})
        user = payload.get('sub')
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return user
    except JWTError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
