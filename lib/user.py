class User():
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(Id: {self.id}, Name: {self.name}, Email: {self.email})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        