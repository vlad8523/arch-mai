"""added username

Revision ID: 34aec1f2d005
Revises: 9874b3bc1a41
Create Date: 2024-05-21 20:53:03.535207

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '34aec1f2d005'
down_revision: Union[str, None] = '9874b3bc1a41'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(), nullable=True))
    # ### end Alembic commands ###

    op.execute('INSERT INTO public."user"(username, password, first_name, second_name, email, is_driver) VALUES ' + \
               "('vladushek', 'Pe&6>52ZDn27306d', 'Vladislav', 'Svinarenko', 'vladushek@mail.ru', true)")
    op.execute('INSERT INTO public."user"(username, password, first_name, second_name, email, is_driver) VALUES ' + \
               "('vaspup', 'honQ?0*oL4|2:Oc:', 'Vasya', 'Pupkin', 'test@mail.ru', false)")
    op.execute('INSERT INTO public."user"(username, password, first_name, second_name, email, is_driver) VALUES ' + \
               "('chernal', 'xDQY&1|0I7m7%\xa', 'Alina', 'Chernygovna', 'chern@mail.ru', false)")
    op.execute('INSERT INTO public."user"(username, password, first_name, second_name, email, is_driver) VALUES ' + \
               "('goland', 'QxsvkYqa1MES6u3o', 'Andrey', 'Golovinsky', 'golovand@mail.ru', true)") 
              


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'username')
    # ### end Alembic commands ###