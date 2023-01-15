"""Adding games table

Revision ID: 333ea2c313fd
Revises: 6ecc439958fa
Create Date: 2023-01-02 22:22:31.614262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '333ea2c313fd'
down_revision = '6ecc439958fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('location_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('games')
    # ### end Alembic commands ###