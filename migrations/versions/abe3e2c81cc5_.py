"""empty message

Revision ID: abe3e2c81cc5
Revises: 744ef7bc83d9
Create Date: 2022-12-06 20:25:30.026387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abe3e2c81cc5'
down_revision = '744ef7bc83d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('money', sa.Integer(), nullable=True))
    op.drop_column('order', 'price')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('price', sa.INTEGER(), nullable=True))
    op.drop_column('order', 'money')
    # ### end Alembic commands ###
