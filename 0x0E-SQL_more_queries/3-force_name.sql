-- Creates a table and VARCHAR(256) can’t be null
-- Creates the table force_name on your MySQL server.
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
