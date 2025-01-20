from pydantic import BaseModel, field_validator
from services.UserAuth.models.user_base_model import TokenData


class TokensRefreshModel(BaseModel):
    status: str
    data: TokenData

    @field_validator("status")
    def validate_status(cls, value):
        if value != "success":
            raise ValueError("Invalid status: must be 'success'.")
        return value
