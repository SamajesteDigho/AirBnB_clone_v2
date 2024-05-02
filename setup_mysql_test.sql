-- Script for preparing the database
-- Create the database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
use hbnb_test_db;

-- Create a user and set his password
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';

-- Grant the given user specific priviledges
GRANT ALL ON hbnb_test_db.* TO hbnb_test@localhost;

-- Grant specific priviledge of specific table
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;
