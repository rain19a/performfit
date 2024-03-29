"""add user id to db

Revision ID: 944004ae89c4
Revises: 0594c71c272b
Create Date: 2024-02-09 12:42:18.645290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '944004ae89c4'
down_revision = '0594c71c272b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('training', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_training_user', 'user', ['user_id'], ['id'])

    with op.batch_alter_table('training_day', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_training_day_user', 'user', ['user_id'], ['id'])

    with op.batch_alter_table('training_inhalt', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_training_inhalt_user', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('training_inhalt', schema=None) as batch_op:
        batch_op.drop_constraint('fk_training_inhalt_user', type_='foreignkey')
        batch_op.drop_column('user_id')

    with op.batch_alter_table('training_day', schema=None) as batch_op:
        batch_op.drop_constraint('fk_training_day_user', type_='foreignkey')
        batch_op.drop_column('user_id')

    with op.batch_alter_table('training', schema=None) as batch_op:
        batch_op.drop_constraint('fk_training_user', type_='foreignkey')
        batch_op.drop_column('user_id')
    # ### end Alembic commands ###
