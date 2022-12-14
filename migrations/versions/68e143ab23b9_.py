"""empty message

Revision ID: 68e143ab23b9
Revises: cc79fe00aa34
Create Date: 2022-08-21 15:45:21.083942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68e143ab23b9'
down_revision = 'cc79fe00aa34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), nullable=False),
    sa.Column('body', sa.VARCHAR(length=225), nullable=False),
    sa.Column('data_created', sa.DATETIME(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
