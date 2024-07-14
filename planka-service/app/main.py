from fastapi import FastAPI
from app.routers import updates
import asyncio
from app.internal.api import PlankaAPIClient
from app.config import PLANKA_URL, EMAIL, PASSWORD

app = FastAPI()

app.include_router(updates.router, prefix="/api")


@app.on_event("startup")
async def startup_event():
    # init_planka()
    from app.internal.updater import start_periodic_update
    planka = PlankaAPIClient(PLANKA_URL, EMAIL, PASSWORD)
    asyncio.create_task(start_periodic_update(planka))
