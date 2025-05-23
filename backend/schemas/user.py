from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    phone: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str
