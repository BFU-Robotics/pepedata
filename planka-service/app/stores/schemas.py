from pydantic import BaseModel
from datetime import datetime

from datetime import datetime
from pydantic import BaseModel
from typing import Optional


# Project Models
class ProjectBase(BaseModel):
    project_id: str
    name: Optional[str] = None
    read: Optional[bool] = False


class ProjectIn(ProjectBase):
    pass


class ProjectOut(ProjectBase):
    id: int
    updated_at: datetime

    class Config:
        orm_mode: True


# Board Models
class BoardBase(BaseModel):
    board_id: str
    project_id: Optional[str] = None
    name: Optional[str] = None
    read: Optional[bool] = False


class BoardIn(BoardBase):
    pass


class BoardOut(BoardBase):
    id: int
    updated_at: datetime

    class Config:
        orm_mode: True


# Card Models
class CardBase(BaseModel):
    card_id: str
    board_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    read: Optional[bool] = False


class CardIn(CardBase):
    pass


class CardOut(CardBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode: True
