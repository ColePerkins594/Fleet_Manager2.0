--Database definitions
DROP DATABASE IF EXISTS "Fleet_Manager_2.0"
CREATE DATABASE "Fleet_Manager_2.0"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LOCALE_PROVIDER = 'libc'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

--Type definitions
--Enums
DROP TYPE IF EXISTS user_role
CREATE TYPE user_role as ENUM(
    "ADMIN",
    "OPERATOR",
    "MECHANIC"
);
--classes
DROP TYPE IF EXISTS "address"

--Table definitions
DROP TABLE IF EXISTS account

CREATE TABLE account(
    account_id SERIAL PRIMARY KEY,
    name varchar(50) NOT NULL,
);

DROP TABLE IF EXISTS user
CREATE TABLE user(
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    role user_role,
    age int
);

