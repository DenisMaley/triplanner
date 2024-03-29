"""trip and trip day tables

Revision ID: 397f2799a5e5
Revises: 11e15c4ec240
Create Date: 2019-09-13 17:00:16.566993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '397f2799a5e5'
down_revision = '11e15c4ec240'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trip',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_trip_timestamp'), 'trip', ['timestamp'], unique=False)
    op.create_index(op.f('ix_trip_user_id'), 'trip', ['user_id'], unique=False)
    op.create_table('trip_day',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=140), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['trip_id'], ['trip.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_trip_day_date'), 'trip_day', ['date'], unique=False)
    op.create_index(op.f('ix_trip_day_trip_id'), 'trip_day', ['trip_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_trip_day_trip_id'), table_name='trip_day')
    op.drop_index(op.f('ix_trip_day_date'), table_name='trip_day')
    op.drop_table('trip_day')
    op.drop_index(op.f('ix_trip_user_id'), table_name='trip')
    op.drop_index(op.f('ix_trip_timestamp'), table_name='trip')
    op.drop_table('trip')
    # ### end Alembic commands ###
