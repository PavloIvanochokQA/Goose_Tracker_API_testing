from pydantic import BaseModel, field_validator


class BadRequestModel(BaseModel):
    success: bool = False
    message: str

    @field_validator("message")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError('Field is empty.')
        else:
            return value
