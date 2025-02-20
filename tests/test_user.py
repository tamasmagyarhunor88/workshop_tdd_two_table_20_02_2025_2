from lib.user import User

def test_user_instantiates():
    user = User(1, 'Hunor', 'hunor@makers.tech')

    assert user.id == 1
    assert user.name == 'Hunor'
    assert user.email == 'hunor@makers.tech'

def test_user_prints_nicely():
    user = User(1, 'Hunor', 'hunor@makers.tech')

    assert str(user) == 'User(Id: 1, Name: Hunor, Email: hunor@makers.tech)'

def test_two_users_with_same_properties_equal():
    user_a = User(1, 'Hunor', 'hunor@makers.tech')
    user_b = User(1, 'Hunor', 'hunor@makers.tech')

    assert user_a == user_b