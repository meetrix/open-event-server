"""empty message

Revision ID: f6e303f33d28
Revises: a79f1dc2fd67
Create Date: 2018-06-29 15:36:45.543502

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'f6e303f33d28'
down_revision = 'a79f1dc2fd67'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ticket_holders', 'lastname',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_constraint('ticket_event', 'ticket_holders', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('ticket_event', 'ticket_holders', ['ticket_id'])
    op.alter_column('ticket_holders', 'lastname',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
