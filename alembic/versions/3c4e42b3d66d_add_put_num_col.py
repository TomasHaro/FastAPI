"""add put num col

Revision ID: 3c4e42b3d66d
Revises: fb8e19f75cd9
Create Date: 2023-01-26 17:28:14.111698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c4e42b3d66d'
down_revision = 'fb8e19f75cd9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("address",sa.Column("apt_numb", sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column("address", "apt_numb")