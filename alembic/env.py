from __future__ import annotations
from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy import engine_from_config
from alembic import context
import os


from app.core.db import Base
from app.models.todo import * # noqa: F401,F403


config = context.config
if config.config_file_name is not None:
fileConfig(config.config_file_name)


def run_migrations_offline() -> None:
context.configure(
url=os.getenv("DATABASE_URL", config.get_main_option("sqlalchemy.url")).replace("+asyncpg", ""),
target_metadata=Base.metadata,
literal_binds=True,
compare_type=True,
)
with context.begin_transaction():
context.run_migrations()


def run_migrations_online() -> None:
connectable = engine_from_config(
{
**config.get_section(config.config_ini_section),
"sqlalchemy.url": os.getenv("DATABASE_URL", config.get_main_option("sqlalchemy.url")).replace("+asyncpg", ""),
},
prefix="sqlalchemy.",
poolclass=pool.NullPool,
)


with connectable.connect() as connection:
context.configure(
connection=connection, target_metadata=Base.metadata, compare_type=True
)
with context.begin_transaction():
context.run_migrations()


if context.is_offline_mode():
run_migrations_offline()
else:
run_migrations_online()
