from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.schemas.task import TaskCreate, Task
from app.crud.task import create_task, get_tasks, get_task, update_task, delete_task
from app.utils.security import decode_access_token
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter()

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return payload

@router.post("/tasks", response_model=Task)
async def create_new_task(task: TaskCreate, db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user = get_current_user(token)
    return await create_task(db, task, user_id=user["sub"])

@router.get("/tasks", response_model=list[Task])
async def read_tasks(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user = get_current_user(token)
    return await get_tasks(db, skip=skip, limit=limit)

@router.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int, db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    task = await get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=Task)
async def update_existing_task(task_id: int, task: TaskCreate, db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_task = await get_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return await update_task(db, db_task, task)

@router.delete("/tasks/{task_id}")
async def delete_existing_task(task_id: int, db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_task = await get_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return await delete_task(db, db_task)
