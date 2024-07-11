from fastapi import FastAPI
from app.routers import updates
import asyncio
from app.stores.database import init_db
from app.internal.updater import init_planka

app = FastAPI()

app.include_router(updates.router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    # init_planka()
    from app.internal.updater import start_periodic_update
    init_db()
    asyncio.create_task(start_periodic_update())
