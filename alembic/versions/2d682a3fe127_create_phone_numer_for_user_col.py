"""create phone numer for user col

Revision ID: 2d682a3fe127
Revises: 
Create Date: 2023-01-26 17:04:15.019925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d682a3fe127'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('phone number', sa.Integer(), nullable=True))


def downgrade() -> None:
    pass
