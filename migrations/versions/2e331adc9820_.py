"""empty message

Revision ID: 2e331adc9820
Revises: 7cae6e35e4a6
Create Date: 2022-04-29 07:57:33.270145

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e331adc9820'
down_revision = '7cae6e35e4a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('character', sa.Column('created', sa.DateTime(), nullable=True))
    op.add_column('character', sa.Column('edited', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('character', 'edited')
    op.drop_column('character', 'created')
    # ### end Alembic commands ###
