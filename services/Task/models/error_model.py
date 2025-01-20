from pydantic import BaseModel, field_validator
from typing import Dict, Union


class ErrorModel(BaseModel):
    success: bool = False
    error: Dict[str, Union[str, Dict]]
    message: str

    @field_validator("message")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError('Field is empty.')
        else:
            return value
