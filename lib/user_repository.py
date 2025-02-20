from lib.user import User

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