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

# def test_create_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = ArtistRepository(db_connection)

#     repository.create(Artist(None, "The Beatles", "Rock"))

#     result = repository.all()
#     assert result == [
#         Artist(1, "Pixies", "Rock"),
#         Artist(2, "ABBA", "Pop"),
#         Artist(3, "Taylor Swift", "Pop"),
#         Artist(4, "Nina Simone", "Jazz"),
#         Artist(5, "The Beatles", "Rock"),
#     ]

# def test_delete_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = ArtistRepository(db_connection)
#     repository.delete(3)

#     result = repository.all()
#     assert result == [
#         Artist(1, "Pixies", "Rock"),
#         Artist(2, "ABBA", "Pop"),
#         Artist(4, "Nina Simone", "Jazz"),
#     ]