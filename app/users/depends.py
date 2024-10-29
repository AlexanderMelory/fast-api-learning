from fastapi import HTTPException, status
from starlette.requests import Request


def get_token(request: Request):
    if token := request.headers.get('booking_access_token'):
        return token
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

def get_current_user(token):
    return 'user'