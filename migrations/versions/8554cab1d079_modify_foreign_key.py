"""Modify foreign key

Revision ID: 8554cab1d079
Revises: d61cadc7c125
Create Date: 2023-01-05 19:25:20.809302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8554cab1d079'
down_revision = 'd61cadc7c125'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointments', sa.Column('game_location', sa.String(length=50), nullable=True))
    op.drop_constraint('appointments_location_game_id_fkey', 'appointments', type_='foreignkey')
    op.create_foreign_key(None, 'appointments', 'games', ['game_location'], ['location'])
    op.drop_column('appointments', 'location_game_id')
    op.drop_column('appointments', 'location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointments', sa.Column('location', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.add_column('appointments', sa.Column('location_game_id', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'appointments', type_='foreignkey')
    op.create_foreign_key('appointments_location_game_id_fkey', 'appointments', 'games', ['location_game_id'], ['id'])
    op.drop_column('appointments', 'game_location')
    # ### end Alembic commands ###
