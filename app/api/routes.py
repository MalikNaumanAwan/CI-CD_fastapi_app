from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.core.db import get_db
from app.schemas.todo import TodoCreate, TodoRead
from app.crud import todo as crud


router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/", response_model=list[TodoRead])
async def get_todos(db: AsyncSession = Depends(get_db)):
    return await crud.list_todos(db)


@router.post("/", response_model=TodoRead, status_code=201)
async def create_todos(payload: TodoCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_todo(db, payload)


@router.post("/{todo_id}/done", status_code=204)
async def mark_done(todo_id: UUID, db: AsyncSession = Depends(get_db)):
    await crud.toggle_todo(db, todo_id)
    return None


@router.delete("/{todo_id}", status_code=204)
async def remove(todo_id: UUID, db: AsyncSession = Depends(get_db)):
    await crud.delete_todo(db, todo_id)
    return None
