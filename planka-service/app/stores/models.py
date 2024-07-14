from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, func, ForeignKey
from datetime import datetime

from app.stores.database import Base

metadata = Base.metadata


class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(String, unique=True, nullable=False)
    name = Column(String)
    updated_at = Column(DateTime, server_default=func.now(),
                        onupdate=func.now())
    read = Column(Boolean, default=False)


class Board(Base):
    __tablename__ = 'boards'
    id = Column(Integer, primary_key=True, autoincrement=True)
    board_id = Column(String, unique=True, nullable=False)
    project_id = Column(ForeignKey('projects.project_id'), nullable=False)
    name = Column(String)
    updated_at = Column(DateTime, server_default=func.now(),
                        onupdate=func.now())
    read = Column(Boolean, default=False)


class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True, autoincrement=True)
    card_id = Column(String, unique=True, nullable=False)
    board_id = Column(ForeignKey('boards.board_id'), nullable=False)
    project_id = Column(ForeignKey('projects.project_id'), nullable=False)
    name = Column(String)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, server_default=func.now(),
                        onupdate=func.now())
    read = Column(Boolean, default=False)
