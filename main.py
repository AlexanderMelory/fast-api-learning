from pydantic.fields import ModelField
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
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, default=True)


class UserDAL:
    """
    Data Access Layer for operating user info
    """

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(self, name: str, surname: str, email: EmailStr) -> User:
        new_user = User(name=name, surname=surname, email=email)
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user


LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z]+$")


class TunedModel(BaseModel):
    """
    Abstract Model
    """

    class Config:
        """
        Convert even non-dict objs to json
        """

        orm_mode = True


class ShowUser(TunedModel):
    user_id = uuid.UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool


class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr

    @validator('name', 'surname')
    def validate_name(cls, value: str, field: ModelField) -> None:
        print(f'{value = }')
        print(f'{field = }')
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=422, detail=f'{field.name} should contains only letters')


app = FastAPI(title='Learning FastAPI')
user_router = APIRouter()


async def _create_user(body: UserCreate) -> ShowUser:
    async with async_session() as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.create_user(name=body.name, surname=body.surname, email=body.email)
            return ShowUser(
                user_id=user.user_id,
                name=user.name,
                surname=user.surname,
                email=EmailStr(user.email),
                is_active=user.is_active,
            )


@user_router.post('/', response_model=ShowUser)
async def create_user(body: UserCreate) -> ShowUser:
    return await _create_user(body)


main_api_router = APIRouter()
main_api_router.include_router(user_router, prefix='/user', tags=['user'])
app.include_router(main_api_router)


if __name__ == '__main__':
    uvicorn.run(app)
