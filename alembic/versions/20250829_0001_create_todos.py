from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "20250829_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto;")
op.create_table(
"todos",
sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
sa.Column("title", sa.String(length=200), nullable=False),
sa.Column("completed", sa.Boolean(), nullable=False, server_default=sa.text("false")),
)


def downgrade() -> None:
op.drop_table("todos")
