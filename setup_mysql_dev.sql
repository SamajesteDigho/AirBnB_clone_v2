-- Script for preparing the database
-- Create the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
use hbnb_dev_db;

-- Create a user and set his password
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant the given user specific priviledges
GRANT ALL ON hbnb_dev_db.* TO hbnb_dev@localhost;

-- Grant specific priviledge of specific table
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
