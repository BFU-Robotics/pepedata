import requests
import asyncio
from pprint import pprint
from datetime import datetime
from sqlalchemy.orm import Session
from app.stores.database import SessionLocal
from app.internal.api import PlankaAPIClient


# async def get_auth_token():
#     planka = Planka(PLANKA_URL, EMAIL, PASSWORD)
#     return planka.auth
# response = requests.post(f"{PLANKA_URL}/users/signin", json={"email": EMAIL, "password": PASSWORD})
# response.raise_for_status()
# return response.json()["token"]


async def collect_updates(planka: PlankaAPIClient):
    pass

    # token = await get_auth_token()

    # Get boards
    # response = requests.get(f"{PLANKA_URL}/api/boards", headers=headers)
    # print(token)
    # print("RESP RESP ", response.status_code, flush=True)
    # print(response.text, flush=True)
    # response.raise_for_status()
    # boards = response.json()

    # db: Session = SessionLocal()

    # for board in boards:
    #     board_id = board['id']
    #     board_name = board['name']

    #     # Get updates for each board
    #     response = requests.get(f"{PLANKA_URL}/api/boards/{board_id}/activities", headers=headers)
    #     response.raise_for_status()
    #     updates = response.json()

    #     # Process the updates as needed
    #     print(f"Updates for board {board_name}:")

    #     # Check if the board exists in the database
    #     db_board = db.query(BoardModel).filter(BoardModel.planka_id == board_id).first()

    #     if not db_board:
    #         # Add new board to the database
    #         new_board = BoardModel(planka_id=board_id, name=board_name, last_update=datetime.utcnow())
    #         db.add(new_board)
    #         db.commit()
    #         db.refresh(new_board)
    #     else:
    #         # Update the last update time
    #         db_board.last_update = datetime.utcnow()
    #         db.commit()

    #     for update in updates:
    #         # Check if the update already exists in the database
    #         db_update = db.query(UpdateModel).filter(UpdateModel.board_id == db_board.id, UpdateModel.timestamp == update['createdAt']).first()
    #         if not db_update:
    #             new_update = UpdateModel(board_id=db_board.id, timestamp=update['createdAt'], description=update['text'])
    #             db.add(new_update)
    #             db.commit()
    #             db.refresh(new_update)

    #         print(update)

    # db.close()


# async def collect_projects(planka: PlankaAPIClient):
#     projects = await planka.get_projects()
#     for project in projects:
#         db_project = await db.execute(select(Project).filter_by(project_id=project['id']))
#         db_project = db_project.scalar_one_or_none()
#         if db_project is None:
#             new_project = Project(
#                 project_id=project['id'], name=project['name'])
#             db.add(new_project)
#         else:
#             db_project.name = project['name']
#             db_project.updated_at = datetime.utcnow()
#             db_project.read = False
#     await db.commit()


async def start_periodic_update(planka: PlankaAPIClient):
    while True:
        await collect_updates(planka)
        await asyncio.sleep(100000)
