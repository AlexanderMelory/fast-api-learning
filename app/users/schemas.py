from pydantic import BaseModel, EmailStr


class SUserRegister(BaseModel):
    name: str
    phone: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class SUserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True
