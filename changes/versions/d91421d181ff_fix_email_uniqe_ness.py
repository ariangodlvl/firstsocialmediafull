"""fix email uniqe ness

Revision ID: d91421d181ff
Revises: de88f04234c2
Create Date: 2026-11-25 10:18:44.532870

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd91421d181ff'
down_revision: Union[str, Sequence[str], None] = 'de88f04234c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("user","email",type_=sa.String , nullable=True , unique=True)


def downgrade() -> None:
    op.alter_column("user","email",type_=sa.String , nullable=True )
