"""Add relationships between Product and Audit

Revision ID: e0060fd0b3d2
Revises: 8cba1f54cc2c
Create Date: 2024-09-18 15:09:59.022872

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0060fd0b3d2'
down_revision: Union[str, None] = '8cba1f54cc2c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('_price', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'products', ['name'])
    op.drop_column('products', 'price')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('price', sa.INTEGER(), nullable=False))
    op.drop_constraint(None, 'products', type_='unique')
    op.drop_column('products', '_price')
    # ### end Alembic commands ###