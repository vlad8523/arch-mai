"""initial migrate

Revision ID: 277077910120
Revises: 
Create Date: 2024-05-10 18:10:24.996561

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '277077910120'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('second_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('is_driver', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # op.execute('INSERT INTO public."user"(first_name, second_name, email, is_driver) VALUES ' + \
    #            "('Vladislav', 'Svinarenko', 'vladushek@mail.ru', true)")
    # op.execute('INSERT INTO public."user"(first_name, second_name, email, is_driver) VALUES ' + \
    #            "('Vasya', 'Pupkin', 'test@mail.ru', false)")
    # op.execute('INSERT INTO public."user"(first_name, second_name, email, is_driver) VALUES ' + \
    #            "('Alina', 'Chernygovna', 'chern@mail.ru', true)")
    # op.execute('INSERT INTO public."user"(first_name, second_name, email, is_driver) VALUES ' + \
    #            "('Andrey', 'Golovinsky', 'golovand@mail.ru', true)") 
              
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
