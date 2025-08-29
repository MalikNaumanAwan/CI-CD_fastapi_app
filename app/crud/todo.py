from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from app.models.todo import Todo
from app.schemas.todo import TodoCreate


async def create_todo(db: AsyncSession, payload: TodoCreate) -> Todo:
    todo = Todo(title=payload.title)
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return todo


async def list_todos(db: AsyncSession) -> list[Todo]:
    res = await db.execute(select(Todo).order_by(Todo.id))
    return list(res.scalars())


async def toggle_todo(db: AsyncSession, todo_id):
    await db.execute(update(Todo).where(Todo.id == todo_id).values(completed=True))
    await db.commit()


async def delete_todo(db: AsyncSession, todo_id):
    await db.execute(delete(Todo).where(Todo.id == todo_id))
    await db.commit()
