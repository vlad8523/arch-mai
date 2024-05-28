from models.domain.user import UserCreate


test_data = [
    UserCreate.model_validate({
        'username': 'vladushek',
        'password': 'Pe&6>52ZDn27306d',
        'email': 'vladushek@mail.ru',
        'first_name': 'Vladislav',
        'second_name': 'Svinarenko',
        'is_driver': True
    }),
    UserCreate.model_validate({
        'username': 'vaspup',
        'password': 'honQ?0*oL4|2:Oc:',
        'email': 'test@mail.ru',
        'first_name': 'Vasya',
        'second_name': 'Pupkin',
        'is_driver': False
    }),
    UserCreate.model_validate({
        'username': 'chernal',
        'password': 'xDQY&1|0I7m7b1xa',
        'email': 'chern@mail.ru',
        'first_name': 'Alina',
        'second_name': 'Chernygovna',
        'is_driver': False
    }),
    UserCreate.model_validate({
        'username': 'goland',
        'password': 'QxsvkYqa1MES6u3o',
        'email': 'golovand@mail.ru',
        'first_name': 'Andrey',
        'second_name': 'Golovinsky',
        'is_driver': True
    })]

