from lib.user_repository import UserRepository
from lib.user import User
from lib.post import Post

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

def test_user_repo_can_fetch_users_posts(db_connection):
    db_connection.seed("seeds/users.sql")
    db_connection.seed("seeds/posts.sql")

    repository = UserRepository(db_connection)
    user = repository.find(1)

    user_posts = repository.posts(user.id)

    assert user_posts == [
        Post(1, 'Its a beautiful life', 1)
    ]

def test_user_repo_can_return_user_with_its_posts(db_connection):
    db_connection.seed("seeds/users.sql")
    db_connection.seed("seeds/posts.sql")

    repository = UserRepository(db_connection)
    user_no_posts = repository.find(1)
    print(user_no_posts)

    user = repository.get_user_with_posts(1)
    print(user)
    print(user.posts)

    assert user.name == 'Sarah'
    assert user.email == 'sarah@software.com'
    assert user.posts == [
        Post(1, 'Its a beautiful life', 1)
    ]
