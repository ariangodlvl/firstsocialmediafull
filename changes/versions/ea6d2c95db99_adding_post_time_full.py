"""adding post time full

Revision ID: ea6d2c95db99
Revises: c997ab1cc36b
Create Date: 2026-11-15 13:15:01.325534

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ea6d2c95db99'
down_revision: Union[str, Sequence[str], None] = 'c997ab1cc36b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column( "timecat", sa.TIMESTAMP(timezone=True),
    server_default=sa.func.now(),
    nullable=False))


def downgrade() -> None:
    op.drop_column("posts","timecat")
