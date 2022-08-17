"""empty message

Revision ID: 75ee43ddc0e5
Revises: 868ac4488929
Create Date: 2022-08-17 12:57:08.685882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75ee43ddc0e5'
down_revision = '868ac4488929'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('phone_num', 'user')


def downgrade():
    pass
