from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.stores import models, schemas
from app.dependencies import get_db

router = APIRouter()


@router.get("/boards/", response_model=list[schemas.BoardOut])
def read_boards(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    boards = db.query(models.Board).offset(skip).limit(limit).all()
    return boards


@router.get("/projects/", response_model=list[schemas.ProjectOut])
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(models.Project).all()

    return projects


@router.get("/cards/", response_model=list[schemas.CardOut])
def get_cards(db: Session = Depends(get_db)):
    cards = db.query(models.Card).all()

    return cards
