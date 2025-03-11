"""Initial migration

Revision ID: 769928da07d7
Revises: 
Create Date: 2025-03-11 20:50:19.050579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '769928da07d7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(length=3), nullable=False),
    sa.Column('nama', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('nomer_telepon', sa.String(length=13), nullable=False),
    sa.Column('alamat', sa.String(length=250), nullable=True),
    sa.Column('poin', sa.Float(), nullable=True),
    sa.Column('img_profil', sa.String(length=250), nullable=True),
    sa.Column('role', sa.String(length=4), nullable=True),
    sa.Column('is_verified', sa.Boolean(), nullable=True),
    sa.Column('verification_code', sa.String(length=6), nullable=True),
    sa.Column('verification_expiry', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nomer_telepon')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
