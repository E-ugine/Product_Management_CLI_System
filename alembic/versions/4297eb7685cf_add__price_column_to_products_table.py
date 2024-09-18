from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'e0060fd0b3d2'
down_revision = '8cba1f54cc2c'
branch_labels = None
depends_on = None

def upgrade():
    # Add the column with a default value
    op.add_column('products', sa.Column('_price', sa.Integer(), nullable=False, server_default='0'))
    
    # You may need to update existing rows to ensure they have a valid value for the new column
    op.execute("UPDATE products SET _price = 0 WHERE _price IS NULL")

def downgrade():
    op.drop_column('products', '_price')
