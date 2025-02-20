from lib.post_repository import PostRepository
from lib.post import Post

def test_get_all_records(db_connection):
    db_connection.seed("seeds/posts.sql") 
    repository = PostRepository(db_connection)

    posts = repository.all()

    assert posts == [
        Post(1, "Its a beautiful life", 1),
        Post(2, "Only those who attempt the absurd can achieve the impossible.", 2),
        Post(3, "Only those who will risk going too far can possibly find out how far one can go.", 3)
    ]

def test_get_single_record(db_connection):
    db_connection.seed("seeds/posts.sql")
    repository = PostRepository(db_connection)

    post = repository.find(2)
    assert post == Post(2, "Only those who attempt the absurd can achieve the impossible.", 2)

def test_create_record(db_connection):
    db_connection.seed("seeds/posts.sql")
    repository = PostRepository(db_connection)

    repository.create(Post(None, "I am very happy", 2))

    posts = repository.all()
    assert posts == [
        Post(1, "Its a beautiful life", 1),
        Post(2, "Only those who attempt the absurd can achieve the impossible.", 2),
        Post(3, "Only those who will risk going too far can possibly find out how far one can go.", 3),
        Post(4, "I am very happy", 2)
    ]

def test_delete_record(db_connection):
    db_connection.seed("seeds/posts.sql")
    repository = PostRepository(db_connection)
    repository.delete(3)

    posts = repository.all()
    assert posts == [
        Post(1, "Its a beautiful life", 1),
        Post(2, "Only those who attempt the absurd can achieve the impossible.", 2)
    ]