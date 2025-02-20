class Post():
    def __init__(self, id, content, user_id):
        self.id = id
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f"Post(Id: {self.id}, Content: {self.content}, User_id: {self.user_id})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__