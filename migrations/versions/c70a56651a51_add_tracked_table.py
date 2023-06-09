"""add tracked table

Revision ID: c70a56651a51
Revises: c25938f61f90
Create Date: 2023-04-12 19:42:15.398933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c70a56651a51'
down_revision = 'c25938f61f90'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tracked',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_currency', sa.String(), nullable=False),
    sa.Column('second_currency', sa.String(), nullable=False),
    sa.Column('date_at', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('first_currency', 'second_currency', name='_first_currency_second_currency_uc')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tracked')
    # ### end Alembic commands ###
