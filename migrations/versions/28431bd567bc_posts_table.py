"""posts table

Revision ID: 28431bd567bc
Revises: 30e4b88107e2
Create Date: 2020-06-13 16:13:30.374092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28431bd567bc'
down_revision = '30e4b88107e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('name', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'name')
    # ### end Alembic commands ###
