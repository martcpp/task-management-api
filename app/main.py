from fastapi import FastAPI
from app.api import user, task
from app.db import database

app = FastAPI()

app.include_router(user.router, prefix="/api")
app.include_router(task.router, prefix="/api")

@app.on_event("startup")
async def startup():
    await database.engine.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.engine.dispose()
