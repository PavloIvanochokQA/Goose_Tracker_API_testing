from pydantic import BaseModel, field_validator
from services.Task.models.task_model import TaskModel


class TaskUpdateModel(BaseModel):
    status: str
    task: TaskModel


    @field_validator("status")
    def validate_status(cls, value):
        if value != "success":
            raise ValueError("Invalid status: must be 'success'")
        return value