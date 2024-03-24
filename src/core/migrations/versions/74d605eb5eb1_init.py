"""init

Revision ID: 74d605eb5eb1
Revises: f4d4368ccc60
Create Date: 2024-03-23 22:31:33.389451

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74d605eb5eb1'
down_revision: Union[str, None] = 'f4d4368ccc60'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'emailing', ['email'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'emailing', type_='unique')
    # ### end Alembic commands ###