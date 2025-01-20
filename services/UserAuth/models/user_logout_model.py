from pydantic import BaseModel, field_validator


class UserLogoutModel(BaseModel):
    message: str

    @field_validator("message")
    def validate_logout_message(cls, value):
        if value != "User successfully logout":
            raise ValueError("Invalid message: must be 'User successfully logout'")
        return value
