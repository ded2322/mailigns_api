"""Initial migration

Revision ID: 5e184cc51868
Revises: df626ef9e5c0
Create Date: 2024-01-25 22:24:25.730793

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5e184cc51868"
down_revision: Union[str, None] = "df626ef9e5c0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "mailings",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("client", sa.String(), nullable=False),
        sa.Column("text_mailing", sa.String(), nullable=False),
        sa.Column(
            "date",
            sa.DateTime(),
            server_default=sa.text("TIMEZONE('utc', now())"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["client"], ["clients.email"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("mailings")
    # ### end Alembic commands ###