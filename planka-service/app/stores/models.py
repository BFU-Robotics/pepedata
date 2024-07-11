from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.stores.database import Base

class BoardModel(Base):
    __tablename__ = 'boards'
    id = Column(Integer, primary_key=True, index=True)
    planka_id = Column(Integer, unique=True, index=True)
    name = Column(String, index=True)
    last_update = Column(DateTime)

    updates = relationship("Update", back_populates="board")

class Update(Base):
    __tablename__ = 'updates'
    id = Column(Integer, primary_key=True, index=True)
    board_id = Column(Integer, ForeignKey('boards.id'))
    timestamp = Column(DateTime)
    description = Column(String)

    board = relationship("Board", back_populates="updates")
