"""remove constrain

Revision ID: ca8934f163a9
Revises: ea6d2c95db99
Create Date: 2026-11-15 18:08:37.003706

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca8934f163a9'
down_revision: Union[str, Sequence[str], None] = 'ea6d2c95db99'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint("posts_topic_key", "posts", type_="unique")


def downgrade() -> None:
    """Downgrade schema."""
    pass
