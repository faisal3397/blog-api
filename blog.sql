-- -------------------------------------------------------------
-- TablePlus 3.10.0(348)
--
-- https://tableplus.com/
--
-- Database: blog
-- Generation Time: 2020-12-10 12:43:13.6580
-- -------------------------------------------------------------


-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS comments_id_seq;

-- Table Definition
CREATE TABLE "public"."comments" (
    "id" int4 NOT NULL DEFAULT nextval('comments_id_seq'::regclass),
    "date" timestamp,
    "content" varchar,
    "post_id" int4,
    PRIMARY KEY ("id")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;

-- Table Definition
CREATE TABLE "public"."posts" (
    "id" int4 NOT NULL DEFAULT nextval('posts_id_seq'::regclass),
    "title" varchar,
    "date" timestamp,
    "content" varchar,
    PRIMARY KEY ("id")
);

INSERT INTO "public"."comments" ("id", "date", "content", "post_id") VALUES
('1', '2020-12-08 16:02:48', 'totally agree with your post', '3'),
('3', '2020-12-08 16:02:48', 'totally agree with your post', '3'),
('4', '2020-12-08 16:02:48', 'totally agree with your post', '3'),
('5', '2020-12-08 16:02:48', 'totally agree with your post', '3'),
('2', '2020-12-08 16:02:48', 'totally agree with your post', '3'),
('6', '2020-12-08 16:02:48', 'totally agree with your post', '3'),
('7', '2020-12-08 16:02:48', 'totally agree with your post', '3'),
('8', '2020-12-08 16:02:48', 'totally agree with your post', '3'),
('9', '2020-12-08 16:02:48', 'totally agree with your post', '3'),
('10', '2020-12-08 16:02:48', 'totally agree with your post', '3'),
('11', '2020-12-08 16:02:48', 'totally agree with your post', '3'),
('12', '2020-12-08 16:02:48', 'totally agree with your post', '3'),
('13', '2020-12-08 16:02:48', 'totally agree with your post', '3'),
('14', '2020-12-08 16:02:48', 'totally agree with your post', '3');

INSERT INTO "public"."posts" ("id", "title", "date", "content") VALUES
('1', 'Modified title 123', '2020-12-08 16:53:58', 'Modified content 1232341242'),
('2', 'Modified title 123', '2020-12-08 16:53:58', 'Modified content 1232341242'),
('3', 'Modified title 123', '2020-12-08 16:53:58', 'Modified content 1232341242'),
('4', 'My New Post 3', '2020-12-08 15:53:58', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
('5', 'My New Post 3', '2020-12-08 15:53:58', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
('6', 'My New Post 3', '2020-12-08 15:53:58', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.');

ALTER TABLE "public"."comments" ADD FOREIGN KEY ("post_id") REFERENCES "public"."posts"("id") ON DELETE CASCADE;
