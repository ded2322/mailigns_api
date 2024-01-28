"""Initial migration

Revision ID: 05aed124a3f8
Revises: 7d491dde57ce
Create Date: 2024-01-27 15:18:48.251551

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "05aed124a3f8"
down_revision: Union[str, None] = "7d491dde57ce"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "completed_mailings",
        "date",
        existing_type=postgresql.TIMESTAMP(),
        type_=sa.String(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "completed_mailings",
        "date",
        existing_type=sa.String(),
        type_=postgresql.TIMESTAMP(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
