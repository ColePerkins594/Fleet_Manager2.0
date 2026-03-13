--DROP STATEMENTS
DROP TABLE IF EXISTS issue;
DROP TABLE IF EXISTS service_record;
DROP TABLE IF EXISTS operator_vehicle;
DROP TABLE IF EXISTS contact_point;
DROP TABLE IF EXISTS vehicle;
DROP TABLE IF EXISTS "user";
DROP TABLE IF EXISTS account;
DROP TYPE IF EXISTS user_role;
DROP TYPE IF EXISTS channel;
DROP TYPE IF EXISTS drivetrain_type;
DROP TYPE IF EXISTS service_type;
DROP TYPE IF EXISTS user_address;

--Type definitions
--Enums

CREATE TYPE user_role as ENUM(
    'ADMIN',
    'OPERATOR',
    'MECHANIC'
);

CREATE TYPE user_status as ENUM(
    'ACTIVE',
    'INACTIVE',
    'ON LEAVE'
);

CREATE TYPE vehicle_status as ENUM(
    'OUT OF SERVICE',
    'ON A JOB',
    'AVAILABLE'
);

CREATE TYPE channel AS ENUM(
    'EMAIL',
    'PHONE-SMS',
    'PHONE-VOICE'
);

CREATE TYPE drivetrain_type as ENUM(
    'ICE',
    'EV',
    'HYBRID',
    'PHEV'
);

CREATE TYPE service_type as ENUM(
    'MAINTENANCE',
    'REPAIR',
    'DIAGNOSIS'
);
--classes
CREATE TYPE user_address AS(
    city VARCHAR(100),
    state CHAR(2),
    street VARCHAR(50),
    zip VARCHAR(9),
    num VARCHAR(7)
);

--Table definitions

CREATE TABLE account(
    account_id SERIAL PRIMARY KEY,
    name varchar(50) NOT NULL
);

CREATE TABLE "user"(
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    role user_role NOT NULL,
    status user_status NOT NULL,
    age int NOT NULL,
    addr user_address NOT NULL,
    account_id INTEGER REFERENCES account (account_id)
);

CREATE TABLE contact_point(
    contact_point_id SERIAL PRIMARY KEY,
    channel channel NOT NULL,
    point VARCHAR(75) NOT NULL,
    is_preffered BOOLEAN NOT NULL,
    user_id INTEGER REFERENCES "user" (user_id)
);

CREATE TABLE vehicle(
    vin VARCHAR(17) PRIMARY KEY,
    make VARCHAR(30) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INTEGER NOT NULL,
    trim VARCHAR(50),
    milage INTEGER,
    drivetrain drivetrain_type NOT NULL,
    efficiency VARCHAR(20),
    range REAL,
    license_plate VARCHAR(15) NOT NULL,
    uptime REAL NOT NULL,
    status vehicle_status NOT NULL,
    insert_date TIMESTAMP NOT NULL,
    account_id INTEGER REFERENCES account (account_id)
);

CREATE TABLE service_record(
    service_record_id SERIAL PRIMARY KEY,
    service_type service_type NOT NULL,
    description TEXT NOT NULL,
    service_date TIMESTAMP NOT NULL,
    completed_time TIMESTAMP,
    vehicle_id VARCHAR(17) REFERENCES vehicle (vin),
    mechanic_id INTEGER REFERENCES "user" (user_id)
);

CREATE TABLE issue(
    issue_id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    symptoms TEXT NOT NULL,
    solution TEXT,
    reported_time TIMESTAMP NOT NULL,
    resolved_time TIMESTAMP,
    service_record_id INTEGER REFERENCES service_record (service_record_id),
    vehicle_id VARCHAR(17) REFERENCES vehicle (vin)
);

CREATE TABLE job(
    job_id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP,
    vehicle_id VARCHAR(17) REFERENCES vehicle (vin),
    operator_id INTEGER REFERENCES "user" (user_id)
);

--Association tables
CREATE TABLE operator_vehicle(
    id SERIAL PRIMARY KEY,
    assign_date TIMESTAMP NOT NULL,
    vehicle_id VARCHAR(17) REFERENCES vehicle (vin),
    operator_id INTEGER REFERENCES "user" (user_id)
);
