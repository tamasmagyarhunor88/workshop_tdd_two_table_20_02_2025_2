class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(Name: {self.name}, Email: {self.email})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        