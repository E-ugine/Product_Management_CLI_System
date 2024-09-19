"""Merge migrations

Revision ID: 6d21b1a5ec6f
Revises: e0060fd0b3d2
Create Date: 2024-09-18 18:01:33.774612

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d21b1a5ec6f'
down_revision: Union[str, None] = 'e0060fd0b3d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
