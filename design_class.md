# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ User(name, email)          │
│                            │
│ - id, name, email          │
│ - posts                    │
│ - posts()                  │
│                            │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Post(content, user_id)  │
│                         │
│ - id, content, user_id  │
│ - user                  │
│ - user()                │
│                         │
└─────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class User:
    # User-facing properties:
    #   id, name, email: data about the user

    def __init__(self, id, name, email):
        pass # No code here yet


class Post:
    # User-facing properties:
    #   id, content, user_id

    def __init__(self, id, content, user_id):
        pass # No code here yet


class UserRepository:
    # methods ommited ...

    def posts():
        pass

class PostRepository:
    # methods  ommited ...

    def user():
        pass

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a user
When user has posts
We see those posts returned when we call posts()
"""
user_repository = UserRepository()
user = user_repository.find(1)
user_posts = user_repository.posts()


user_posts # => [Post(Id: 1, Content: Its a beautiful life, User_id: 1)]

"""
Given a post
When post belongs to a user
We see that user returned when we call user()
"""
post_repository = PostRepository()
post = post_repository.find(1)
post_user = post_repository.user()


post_user # => User(Id: 1, Name: Sarah, Email: sarah@software.com)]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE


```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
