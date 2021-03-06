"""empty message

Revision ID: 63838ca40167
Revises: 5dd04b2f2129
Create Date: 2022-05-02 11:21:10.776532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63838ca40167'
down_revision = '5dd04b2f2129'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('case', sa.Column('confirmed', sa.Integer(), nullable=True))
    op.drop_column('case', 'comfirmed')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('case', sa.Column('comfirmed', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('case', 'confirmed')
    # ### end Alembic commands ###
