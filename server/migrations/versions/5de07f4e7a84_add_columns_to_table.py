"""add columns to table

Revision ID: 5de07f4e7a84
Revises: 67f5d67aea55
Create Date: 2025-06-16 17:58:13.237909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5de07f4e7a84'
down_revision = '67f5d67aea55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plants')
    # ### end Alembic commands ###
