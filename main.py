from sqlalchemy.orm import sessionmaker, declarative_base

import settings
from fastapi import FastAPI, HTTPException
import uvicorn
from fastapi.routing import APIRouter
from sqlalchemy import Column, Boolean, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.dialects.postgresql import UUID
import uuid
import re
from pydantic import BaseModel, EmailStr, validator


# create async engine for interaction with db
engine = create_async_engine(settings.REAL_DATABASE_URL, future=True, echo=True)
# create session for the interaction with db
async_session = sessionmaker(engine, future=True, class_=AsyncSession)

Base = declarative_base()


class User(Base):
    """
    User model
    """
    __tablename__ = 'user'

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(EmailStr, nullable=False, unique=True)
    is_active = Column(Boolean, default=True)


class UserDAL:
    """
    Data Access Layer for operating user info
    """

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(self, name: str, surname: str, email: str) -> User:
        new_user = User(name=name, surname=surname, email=email)
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user
