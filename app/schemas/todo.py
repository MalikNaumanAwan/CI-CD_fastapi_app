from pydantic import BaseModel, Field
from uuid import UUID


class TodoCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)


class TodoRead(BaseModel):
    id: UUID
    title: str
    completed: bool


model_config = {"from_attributes": True}
