# Two Tables Design Recipe Template

_Copy this recipe template to design and create two related database tables from a specification._

## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a business owner,
So I can release my app,
I want to have users.

As a business owner,
So that I can have users,
I want to keep a list of users names.

As a business owner,
So that I can have users,
I want to keep a list of users emails.

As a business owner,
So that I can have a social media platform,
I want my users to have posts.

As a business owner,
So that I my users can have posts,
I want the posts to have content.

As a business owner,
So that I my users can have posts,
I want the posts to have a user_id.
```

```
Nouns:

user, name, email, post, content, user_id
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| user                  | name, email
| post                  | content, user_id |

1. Name of the first table (always plural): `users` 

    Column names: `name`, `email`

2. Name of the second table (always plural): `posts` 

    Column names: `content, user_id`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: users
id: SERIAL
name: text
email: text

Table: posts
id: SERIAL
content: text
user_id: int
```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one [user] have many [post]? (Yes)
2. Can one [post] have many [user]? (No)

You'll then be able to say that:

1. **[user] has many [post]**
2. And on the other side, **[post] belongs to [user]**
3. In that case, the foreign key is in the table [post]

Replace the relevant bits in this example with your own:

```
# EXAMPLE

1. Can one user have many posts? YES
2. Can one post have many users? NO

-> Therefore,
-> A user HAS MANY posts
-> A post BELONGS TO a user

-> Therefore, the foreign key is on the posts table.
```

*If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).*

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: users.sql
-- file: posts.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name text,
  email text
);

-- Then the table with the foreign key second.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  content text,
-- The foreign key name is always {other_table_singular}_id
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 database_name < users.sql
psql -h 127.0.0.1 database_name < posts.sql
```