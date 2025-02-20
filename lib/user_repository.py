from lib.user import User
from lib.post import Post

class UserRepository():
    def __init__(self, db_connection):
        self._db_connection = db_connection

    def all(self):
        users_rows = self._db_connection.execute("SELECT * FROM users")

        users = []

        for user_dict in users_rows:
            user = User(user_dict['id'], user_dict['name'], user_dict['email'])
            users.append(user)
        
        return users

    def find(self, user_id):
        users_rows = self._db_connection.execute("SELECT * FROM users WHERE id = %s", [user_id])
        user = User(users_rows[0]['id'], users_rows[0]['name'], users_rows[0]['email'])
        return user
    
    def create(self, user):
        self._db_connection.execute(
            "INSERT INTO users (name, email) VALUES(%s, %s)",
            [user.name, user.email]
        )
    
    def delete(self, user_id):
        self._db_connection.execute("DELETE FROM users WHERE id = %s", [user_id])
    
    def posts(self, user_id):
        posts = []

        rows = self._db_connection.execute("SELECT * FROM posts WHERE user_id = %s", [user_id])
        for post_dict in rows:
            post = Post(post_dict['id'], post_dict['content'], post_dict['user_id'])
            posts.append(post)

        return posts

    def get_user_with_posts(self, user_id):
        user = self.find(user_id)

        user.posts = self.posts(user_id)

        return user