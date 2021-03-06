"""empty message

Revision ID: 1e5ac30eeb4d
Revises: 1e55a25f0325
Create Date: 2020-05-19 15:20:09.998107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e5ac30eeb4d'
down_revision = '1e55a25f0325'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('item_type', sa.String(length=64), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'item_type')
    # ### end Alembic commands ###
