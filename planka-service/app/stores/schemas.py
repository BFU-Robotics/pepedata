from pydantic import BaseModel
from datetime import datetime

class BoardBase(BaseModel):
    planka_id: int
    name: str

class BoardCreate(BoardBase):
    pass

class BoardUpdate(BaseModel):
    last_update: datetime

class Board(BoardBase):
    id: int
    last_update: datetime

    class Config:
        orm_mode = True

class UpdateBase(BaseModel):
    board_id: int
    timestamp: datetime
    description: str

class UpdateCreate(UpdateBase):
    pass

class Update(UpdateBase):
    id: int

    class Config:
        orm_mode = True
