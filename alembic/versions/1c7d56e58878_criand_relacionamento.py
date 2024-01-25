"""criand relacionamento

Revision ID: 1c7d56e58878
Revises: 16ba91dd88fb
Create Date: 2024-01-24 23:54:10.111790

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c7d56e58878'
down_revision: Union[str, None] = '16ba91dd88fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
