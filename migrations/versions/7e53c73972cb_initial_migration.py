"""Initial migration

Revision ID: 7e53c73972cb
Revises: 
Create Date: 2023-02-08 20:40:12.753111

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7e53c73972cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('persons')
    op.create_table('tasks',
    sa.Column('id', mysql.VARCHAR(length=50), primary_key=True),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('status', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('priority', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('notes', mysql.VARCHAR(length=500), nullable=True),
    sa.Column('created_by', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('assigned_to', mysql.VARCHAR(length=50), nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks')
    # ### end Alembic commands ###