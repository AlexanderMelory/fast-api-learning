from app.dao.base import BaseDAO
from app.users.models import User


class UserDAO(BaseDAO):
    """
    DAO пользователя
    """

    model = User
