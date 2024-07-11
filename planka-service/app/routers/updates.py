from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.stores import models, schemas
from app.stores.database import SessionLocal

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/boards/", response_model=list[schemas.Board])
def read_boards(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    boards = db.query(models.Board).offset(skip).limit(limit).all()
    return boards

@router.get("/boards/{board_id}", response_model=schemas.Board)
def read_board(board_id: int, db: Session = Depends(get_db)):
    board = db.query(models.Board).filter(models.Board.id == board_id).first()
    if board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return board

@router.get("/boards/{board_id}/updates")
def read_board_updates(board_id: int, db: Session = Depends(get_db)):
    board = db.query(models.Board).filter(models.Board.id == board_id).first()
    if board is None:
        raise HTTPException(status_code=404, detail="Board not found")

    # This would ideally fetch updates from an updates table or service.
    # For now, we will return a placeholder response
    updates = [
        {"update": "Sample update 1", "timestamp": "2023-07-07T10:00:00Z"},
        {"update": "Sample update 2", "timestamp": "2023-07-08T10:00:00Z"},
    ]

    return {"board_id": board_id, "updates": updates}
