"""remoce and cuurect emain uniqenes

Revision ID: de88f04234c2
Revises: 93bbed7d832a
Create Date: 2026-11-16 20:47:17.678145

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de88f04234c2'
down_revision: Union[str, Sequence[str], None] = '93bbed7d832a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:    
    op.drop_constraint("user_email_key", "user", type_="unique")
    sa.table("user",sa.Column("email" , sa.String , nullable=True , unique=True))

def downgrade() -> None:
    op.create_unique_constraint(
    "user_email_key",
    "user",
    ["email"]
)