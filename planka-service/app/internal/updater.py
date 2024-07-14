import asyncio
from sqlalchemy.orm import Session

import app.stores.models as models
from app.stores.database import SessionLocal
from app.internal.api import PlankaAPIClient


async def collect_projects(planka: PlankaAPIClient, db: Session):
    projects = planka.get_projects()
    for project in projects:
        db_project = db.query(models.Project).filter_by(
            project_id=project['id']
        )

        db_project = db_project.scalar()
        if db_project is None:
            new_project = models.Project(
                project_id=project['id'], name=project['name']
            )

            db.add(new_project)

    db.commit()


async def collect_boards(planka: PlankaAPIClient, db: Session):
    boards = planka.get_boards()
    for board in boards:
        db_board = db.query(models.Board).filter_by(
            board_id=board['id']
        )

        db_board = db_board.scalar()
        if db_board is None:
            new_board = models.Board(
                board_id=board['id'], project_id=board["projectId"],
                name=board['name']
            )

            db.add(new_board)

    db.commit()


async def start_periodic_update(planka: PlankaAPIClient):
    while True:
        db = SessionLocal()
        await collect_projects(planka, db)
        await collect_boards(planka, db)
        await asyncio.sleep(60)
