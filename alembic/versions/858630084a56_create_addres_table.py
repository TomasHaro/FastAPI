"""create addres table

Revision ID: 858630084a56
Revises: 2d682a3fe127
Create Date: 2023-01-26 17:19:49.312508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '858630084a56'
down_revision = '2d682a3fe127'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("address", sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('address1', sa.String(), nullable=False),
                    sa.Column('address2', sa.String(), nullable=False),
                    sa.Column('city', sa.String(), nullable=False),
                    sa.Column('state', sa.String(), nullable=False),
                    sa.Column('country', sa.String(), nullable=False),
                    sa.Column('postalcode', sa.String(), nullable=False)
                    )


def downgrade() -> None:
    op.drop_table("adress")
