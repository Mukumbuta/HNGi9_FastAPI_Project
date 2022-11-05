from pydantic import BaseModel
from enum import Enum

class InputModel(BaseModel):
    operation_type: str
    x: int
    y: int

    # Forbid any other input undefined by the enpoint
    class Config:
        extra = "forbid"


class OutputModel(BaseModel):
    slackUsername = "Emmanuel Simasiku"
    operation_type: str
    result: int
    