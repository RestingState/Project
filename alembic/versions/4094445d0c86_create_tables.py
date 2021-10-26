"""Create tables

Revision ID: 4094445d0c86
Revises: 
Create Date: 2021-10-26 16:29:56.866640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4094445d0c86'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('major',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('subject',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.String(length=64), nullable=False),
    sa.Column('login', sa.String(length=24), nullable=False),
    sa.Column('password', sa.String(length=48), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('login')
    )
    op.create_table('mark',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('grade', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('major_id', sa.Integer(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['major_id'], ['major.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('student_mark',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('mark_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['mark_id'], ['mark.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('student_id', 'mark_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student_mark')
    op.drop_table('student')
    op.drop_table('mark')
    op.drop_table('users')
    op.drop_table('subject')
    op.drop_table('major')
    # ### end Alembic commands ###