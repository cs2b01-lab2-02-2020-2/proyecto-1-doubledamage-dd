"""empty message

Revision ID: a01917928bbb
Revises: 31d2a5d82b00
Create Date: 2020-10-20 14:52:31.748817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a01917928bbb'
down_revision = '31d2a5d82b00'
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
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuarios_nuevos')
    # ### end Alembic commands ###
