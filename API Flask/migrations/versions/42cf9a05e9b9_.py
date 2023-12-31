"""empty message

Revision ID: 42cf9a05e9b9
Revises: 6fcb38bb5a19
Create Date: 2023-10-10 09:15:33.956379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42cf9a05e9b9'
down_revision = '6fcb38bb5a19'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('professor_formacao',
    sa.Column('professor_id', sa.Integer(), nullable=False, prymary_key=True),
    sa.Column('formacao_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['formacao_id'], ['formacao.id'], ),
    sa.ForeignKeyConstraint(['professor_id'], ['professor.id'], ),
    sa.PrimaryKeyConstraint('formacao_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('professor_formacao')
    # ### end Alembic commands ###
