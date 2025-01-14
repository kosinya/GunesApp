import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str = ""
    email: str = ""
    date_of_birth: str = datetime.date.today()
    phone_number: str = None
    is_admin: bool = False
    is_active: bool = True


class CreateUser(UserBase):
    password: str = ""


class User(UserBase):
    id: int

    class Config:
        from_attributes = True
