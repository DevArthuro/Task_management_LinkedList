from pydantic import BaseModel
from enum import Enum

class StatusTask(Enum):
    ACTIVE = True
    DEACTIVE = False


class TaskRegister(BaseModel):
    title: str
    description: str
    status: StatusTask