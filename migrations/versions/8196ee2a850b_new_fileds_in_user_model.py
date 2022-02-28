"""new fileds in user model

Revision ID: 8196ee2a850b
Revises: d8d3ff450820
Create Date: 2022-02-24 14:00:54.787249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8196ee2a850b'
down_revision = 'd8d3ff450820'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###