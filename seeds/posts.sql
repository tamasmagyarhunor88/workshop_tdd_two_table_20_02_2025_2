DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    content VARCHAR(255),
    user_id int
    -- user_id int,
    -- constraint fk_user foreign key(user_id)
    --   references users(id)
    --   on delete cascade
);

INSERT INTO posts (content, user_id) VALUES ('Its a beautiful life', 1);
INSERT INTO posts (content, user_id) VALUES ('Only those who attempt the absurd can achieve the impossible.', 2);
INSERT INTO posts (content, user_id) VALUES ('Only those who will risk going too far can possibly find out how far one can go.', 3);