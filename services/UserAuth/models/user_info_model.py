from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional


class UserInfoModel(BaseModel):
    id: str = Field(..., alias="_id")
    name: str
    email: EmailStr
    accessToken: str
    refreshToken: str
    phone: Optional[str] = None
    birthday: Optional[str] = None
    skype: Optional[str] = None
    userImgUrl: Optional[str] = None
    version: int = Field(0, alias="__v")

    @field_validator("id", "name", "accessToken", "refreshToken")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError('Field is empty.')
        else:
            return value
