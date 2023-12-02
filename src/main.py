import asyncio

import uvicorn
from fastapi import FastAPI

from src.api.routers import all_routers
from src.db.create_db import create_database

app = FastAPI(
    title="Тест"
)


for router in all_routers:
    app.include_router(router=router)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_database())

    uvicorn.run(app="main:app", reload=True)
