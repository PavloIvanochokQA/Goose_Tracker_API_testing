from enum import Enum


class Priority(Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Category(Enum):
    todo = "to-do"
    in_progress = "in-progress"
    done = "done"
