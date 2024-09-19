from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e83c2df127fd'
down_revision = '6d21b1a5ec6f'
branch_labels = None
depends_on = None


def upgrade():
    # Use batch mode for SQLite to allow adding constraints
    with op.batch_alter_table("products", schema=None) as batch_op:
        batch_op.add_column(sa.Column('quantity', sa.Integer(), nullable=False, server_default="1"))
        # Provide a name for the unique constraint
        batch_op.create_unique_constraint('uq_products_name', ['name'])


def downgrade():
    with op.batch_alter_table("products", schema=None) as batch_op:
        batch_op.drop_constraint('uq_products_name', type_='unique')
        batch_op.drop_column('quantity')
