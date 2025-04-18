"""empty message

Revision ID: ada439b03ce9
Revises: ecb416d1152c
Create Date: 2025-03-18 15:36:10.560527

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'ada439b03ce9'
down_revision: Union[str, None] = 'ecb416d1152c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('clientel', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nitrut', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('nombre_empresa', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
        batch_op.add_column(sa.Column('representante', sqlmodel.sql.sqltypes.AutoString(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('clientel', schema=None) as batch_op:
        batch_op.drop_column('representante')
        batch_op.drop_column('nombre_empresa')
        batch_op.drop_column('nitrut')

    # ### end Alembic commands ###
