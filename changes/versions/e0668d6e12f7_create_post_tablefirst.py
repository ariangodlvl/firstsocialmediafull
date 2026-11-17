"""create post tablefirst

Revision ID: e0668d6e12f7
Revises: 
Create Date: 2026-11-15 09:01:14.683772

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0668d6e12f7'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id",sa.Integer,nullable=True,primary_key=True),
        sa.Column("topic",sa.String,nullable=True),
        sa.Column("content",sa.String,nullable=True),
        sa.TIMESTAMP(timezone=True),
        sa.UniqueConstraint("topic"),
        sa.PrimaryKeyConstraint("id")
# datetime.datetime.utcnow().replace(
#   tzinfo=datetime.timezone.utc
# ).astimezone(ZoneInfo(<timezone>)
# timezone - an optional timezone name (e.g. UTC, EST5EDT, etc.) that will be applied to the timestamp which renders inside the migration file’s comment as well as within the filename. This option requires Python>=3.9 or installing the backports.zoneinfo library and the tzdata library. If timezone is specified, the create date object is no longer derived from datetime.datetime.now() and is instead generated as
    )


def downgrade() -> None:
    op.drop_table("posts")
