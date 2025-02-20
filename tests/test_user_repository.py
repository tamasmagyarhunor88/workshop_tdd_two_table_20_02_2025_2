from lib.user_repository import UserRepository
from lib.user import User

def test_get_all_records(db_connection):
    db_connection.seed("seeds/users.sql") 
    repository = UserRepository(db_connection)

    users = repository.all()

    assert users == [
        User(1, "Sarah", "sarah@software.com"),
        User(2, "Xiao", "xiao@software.com"),
        User(3, "Edward", "edward@software.com")
    ]

def test_get_single_record(db_connection):
    db_connection.seed("seeds/users.sql")
    repository = UserRepository(db_connection)

    user = repository.find(2)
    assert user == User(2, "Xiao", "xiao@software.com")

def test_create_record(db_connection):
    db_connection.seed("seeds/users.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, "Anamaria", "anamaria@software.com"))

    users = repository.all()
    assert users == [
        User(1, "Sarah", "sarah@software.com"),
        User(2, "Xiao", "xiao@software.com"),
        User(3, "Edward", "edward@software.com"),
        User(4, "Anamaria", "anamaria@software.com")
    ]

def test_delete_record(db_connection):
    db_connection.seed("seeds/users.sql")
    repository = UserRepository(db_connection)
    repository.delete(3)

    users = repository.all()
    assert users == [
        User(1, "Sarah", "sarah@software.com"),
        User(2, "Xiao", "xiao@software.com")
    ]