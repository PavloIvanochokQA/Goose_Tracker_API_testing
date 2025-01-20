from pydantic import BaseModel
from datetime import datetime
from services.Task.models.task_model import TaskModel


class ListItemModel(BaseModel):
    tasks: list[TaskModel]
    date: datetime
