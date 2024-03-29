"""empty message

Revision ID: 388c9daa9ef5
Revises: 0a062e62351c
Create Date: 2020-10-20 15:25:07.118456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '388c9daa9ef5'
down_revision = '0a062e62351c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios_nuevos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dzname', sa.String(), nullable=False),
    sa.Column('dzEmail', sa.String(), nullable=False),
    sa.Column('dzOther_phone', sa.Integer(), nullable=False),
    sa.Column('dzOther_sex', sa.String(), nullable=False),
    sa.Column('dzMessage', sa.String(), nullable=False),
    sa.Column('dzLogueado', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuarios_nuevos')
    # ### end Alembic commands ###
