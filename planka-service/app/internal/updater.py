import requests
import asyncio
from datetime import datetime
from sqlalchemy.orm import Session
from app.dependencies import PLANKA_URL, EMAIL, PASSWORD, UPDATE_INTERVAL
from app.stores.database import SessionLocal
from app.stores.models import BoardModel, Update as UpdateModel
from app.internal.plankapy import *



def init_planka():
    planka = Planka(PLANKA_URL, EMAIL, PASSWORD)
    board = Board(planka)
    print("ASDASDASDDS")
    print("Auth ", planka.auth, flush=True)


async def get_auth_token():
    planka = Planka(PLANKA_URL, EMAIL, PASSWORD)
    return planka.auth
    # response = requests.post(f"{PLANKA_URL}/users/signin", json={"email": EMAIL, "password": PASSWORD})
    # response.raise_for_status()
    # return response.json()["token"]

async def collect_updates():
    token = await get_auth_token()
    headers = \
            { 
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
            }

    # Get boards
    response = requests.get(f"{PLANKA_URL}/api/boards", headers=headers)
    print(token)
    print("RESP RESP ", response.status_code, flush=True)
    print(response.text, flush=True)
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

async def start_periodic_update():
    while True:
        await collect_updates()
        await asyncio.sleep(100000)
