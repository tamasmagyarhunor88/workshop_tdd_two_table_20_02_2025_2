from lib.post import Post

def test_post_instantiates():
    post = Post(1, 'I love today', 1)

    assert post.id == 1
    assert post.content == 'I love today'
    assert post.user_id == 1

def test_post_formats_nicely():
    post = Post(1, 'I love today', 1)

    assert str(post) == f"Post(Id: 1, Content: I love today, User_id: 1)"

def test_two_posts_same_properties_are_equal():
    post_a = Post(1, 'I love today', 1)
    post_b = Post(1, 'I love today', 1)

    assert post_a == post_b