from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.stores import models, schemas
from app.dependencies import get_db

router = APIRouter()


@router.get("/boards/", response_model=list[schemas.BoardOut])
def read_boards(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    boards = db.query(models.Board).offset(skip).limit(limit).all()
    return boards


@router.get("/boards/new/", response_model=list[schemas.BoardOut])
def get_new_boards(db: Session = Depends(get_db)):
    boards = db.query(models.Board).filter(
        models.Board.read == False).all()

    return boards


@router.put("/boards/read/")
def read_boards(db: Session = Depends(get_db)):
    db.query(models.Board).filter(models.Board.read == False).update(
        {models.Board.read: True})

    boards = db.query(models.Board).filter(
        models.Board.read == False).all()

    if boards:
        raise HTTPException(status_code=400, detail="Error reading boards")

    db.commit()

    return {"ok": True}


@router.get("/projects/", response_model=list[schemas.ProjectOut])
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(models.Project).all()

    return projects


@router.get("/projects/new/", response_model=list[schemas.ProjectOut])
def get_new_projects(db: Session = Depends(get_db)):
    projects = db.query(models.Project).filter(
        models.Project.read == False).all()

    return projects


@router.put("/projects/read/")
def read_projects(db: Session = Depends(get_db)):
    db.query(models.Project).filter(models.Project.read == False).update(
        {models.Project.read: True})

    projects = db.query(models.Project).filter(
        models.Project.read == False).all()

    if projects:
        raise HTTPException(status_code=400, detail="Error reading projects")

    db.commit()

    return {"ok": True}


@router.get("/cards/", response_model=list[schemas.CardOut])
def get_cards(db: Session = Depends(get_db)):
    cards = db.query(models.Card).all()

    return cards


@router.get("/cards/new/", response_model=list[schemas.CardOut])
def get_cards(db: Session = Depends(get_db)):
    cards = db.query(models.Card).filter(models.Card.read == False).all()

    return cards


@router.put("/cards/read/")
def read_cards(db: Session = Depends(get_db)):
    db.query(models.Card).filter(models.Card.read == False).update(
        {models.Card.read: True})

    cards = db.query(models.Card).filter(models.Card.read == False).all()
    if cards:
        raise HTTPException(status_code=400, detail="Error reading cards")

    db.commit()

    return {"ok": True}
