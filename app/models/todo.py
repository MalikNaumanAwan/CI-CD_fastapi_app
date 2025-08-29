from sqlalchemy import Column, String, Boolean, text
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.core.db import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        server_default=text("gen_random_uuid()"),
    )
    title = Column(String(200), nullable=False)
    completed = Column(Boolean, nullable=False, server_default=text("false"))
