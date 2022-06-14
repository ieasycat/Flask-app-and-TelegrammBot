"""empty message

Revision ID: 53c217f0c2b3
Revises: 6edcb4004eef
Create Date: 2022-06-14 23:58:21.400884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53c217f0c2b3'
down_revision = '6edcb4004eef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('employee_data_employee_id_fkey', 'employee_data', type_='foreignkey')
    op.create_foreign_key(None, 'employee_data', 'employee', ['employee_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'employee_data', type_='foreignkey')
    op.create_foreign_key('employee_data_employee_id_fkey', 'employee_data', 'employee_data', ['employee_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
