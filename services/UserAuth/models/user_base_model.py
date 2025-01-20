from pydantic import BaseModel, EmailStr, field_validator


class TokenData(BaseModel):
    accessToken: str
    refreshToken: str

    @field_validator("accessToken", "refreshToken")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError('Field is empty.')
        else:
            return value


class UserBaseModel(BaseModel):
    id: str
    name: str
    email: EmailStr
    data: TokenData

    @field_validator("id", "name")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError('Field is empty.')
        else:
            return value
