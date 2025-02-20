DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

INSERT INTO users (name, email) VALUES ('Sarah', 'sarah@software.com');
INSERT INTO users (name, email) VALUES ('Xiao', 'xiao@software.com');
INSERT INTO users (name, email) VALUES ('Edward', 'edward@software.com');