"""modify Categories

Revision ID: aca82ae23562
Revises: ae0997e3d235
Create Date: 2023-04-14 12:50:51.151989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aca82ae23562'
down_revision = 'ae0997e3d235'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('categories', sa.Column('place_id', sa.Integer, sa.ForeignKey('places.id')))


def downgrade() -> None:
    pass
