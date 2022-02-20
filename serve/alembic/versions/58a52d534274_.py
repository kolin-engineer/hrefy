"""empty message

Revision ID: 58a52d534274
Revises: 479a09df0a09
Create Date: 2022-02-18 09:20:20.510763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58a52d534274'
down_revision = '479a09df0a09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('link', sa.Column('_is_removed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('link', '_is_removed')
    # ### end Alembic commands ###