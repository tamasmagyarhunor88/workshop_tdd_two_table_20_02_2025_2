from lib.post import Post

class PostRepository():
    def __init__(self, db_connection):
        self._db_connection = db_connection

    def all(self):
        posts_rows = self._db_connection.execute("SELECT * FROM posts")

        posts = []

        for post_dict in posts_rows:
            post = Post(post_dict['id'], post_dict['content'], post_dict['user_id'])
            posts.append(post)
        
        return posts
    
    def find(self, post_id):
        posts_rows = self._db_connection.execute("SELECT * FROM posts WHERE id = %s", [post_id])
        post = Post(posts_rows[0]['id'], posts_rows[0]['content'], posts_rows[0]['user_id'])
        return post

    def create(self, post):
        self._db_connection.execute(
            "INSERT INTO posts (content, user_id) VALUES (%s, %s)",
            [post.content, post.user_id]
        )
    
    def delete(self, post_id):
        self._db_connection.execute(
            "DELETE FROM posts WHERE id = %s",
            [post_id]
        )