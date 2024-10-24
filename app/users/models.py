from sqlalchemy import Column, String, Integer

from app.db import Base


class User(Base):
    """
    Пользователь
    """

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(500), nullable=False)
