"""Modifying schema

Revision ID: 42cb8a2f4789
Revises: 333ea2c313fd
Create Date: 2023-01-05 12:20:56.708440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42cb8a2f4789'
down_revision = '333ea2c313fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointments', sa.Column('location_game_id', sa.String(), nullable=True))
    op.add_column('appointments', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'appointments', 'games', ['location_game_id'], ['id'])
    op.drop_column('appointments', 'location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointments', sa.Column('location', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'appointments', type_='foreignkey')
    op.drop_column('appointments', 'user_id')
    op.drop_column('appointments', 'location_game_id')
    # ### end Alembic commands ###
