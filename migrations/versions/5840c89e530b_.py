"""empty message

Revision ID: 5840c89e530b
Revises: 
Create Date: 2023-11-30 22:33:40.929119

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5840c89e530b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=True),
    sa.Column('apellido', sa.String(length=100), nullable=True),
    sa.Column('telefono', sa.String(length=15), nullable=True),
    sa.Column('carrera', sa.String(length=100), nullable=True),
    sa.Column('pais', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('estudiante')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('estudiante',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('apellido', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('telefono', mysql.VARCHAR(length=15), nullable=True),
    sa.Column('carrera', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('pais', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('contact')
    # ### end Alembic commands ###
