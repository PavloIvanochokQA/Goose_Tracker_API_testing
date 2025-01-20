from pydantic import BaseModel, Field, field_validator
from datetime import datetime, time
from utils.enums import Priority, Category


class TaskModel(BaseModel):
    title: str
    start: time
    end: time
    priority: Priority
    category: Category
    owner: str
    date: datetime
    id: str = Field(..., alias="_id")
    createdAt: datetime
    updatedAt: datetime
    version: int = Field(0, alias="__v")

    @field_validator("title", "owner", "id",)
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError('Field is empty.')
        else:
            return value
