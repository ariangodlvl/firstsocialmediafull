"""insta tags like thing

Revision ID: 93bbed7d832a
Revises: ca8934f163a9
Create Date: 2026-11-15 18:15:51.500806

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93bbed7d832a'
down_revision: Union[str, Sequence[str], None] = 'ca8934f163a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("tags",sa.Column("id",sa.Integer, primary_key=True),sa.Column("name", sa.String(), nullable=False, unique=True))
    
    op.create_table("post_tags_connection", sa.Column("post_id",sa.Integer, sa.ForeignKey("posts.id",ondelete="CASCADE"), primary_key=True),
    sa.Column("tag_id",sa.Integer, sa.ForeignKey("tags.id",ondelete="CASCADE"), primary_key=True))

def downgrade() -> None:
    op.drop_table("post_tags_connection")
    op.drop_table("tags")
