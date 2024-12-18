"""add booking, user, room models

Revision ID: 21922b9643c0
Revises: 443d208e4725
Create Date: 2024-10-17 16:50:31.061945

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '21922b9643c0'
down_revision: Union[str, None] = '443d208e4725'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'room',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('number', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('phone', sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'booking',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('room_id', sa.Integer(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('date_from', sa.Date(), nullable=False),
        sa.Column('date_to', sa.Date(), nullable=False),
        sa.Column('price', sa.DECIMAL(), nullable=False),
        sa.Column(
            'total_cost',
            sa.DECIMAL(),
            sa.Computed(
                '(date_to - date_from) * price',
            ),
            nullable=True,
        ),
        sa.Column(
            'total_days',
            sa.Integer(),
            sa.Computed(
                'date_to - date_from',
            ),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ['room_id'],
            ['room.id'],
        ),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['user.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('booking')
    op.drop_table('user')
    op.drop_table('room')
    # ### end Alembic commands ###
