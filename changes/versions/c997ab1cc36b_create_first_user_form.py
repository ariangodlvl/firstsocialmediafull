"""create first user form

Revision ID: c997ab1cc36b
Revises: e0668d6e12f7
Create Date: 2026-11-15 09:05:39.559942

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c997ab1cc36b'
down_revision: Union[str, Sequence[str], None] = 'e0668d6e12f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id",sa.INTEGER,nullable=True),
        sa.Column("email",sa.String,nullable=True),
        sa.Column("password",sa.String,nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email")
        )


def downgrade() -> None:
    op.drop_table("user")
