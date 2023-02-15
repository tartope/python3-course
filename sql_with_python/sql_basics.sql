--  Python comes with a built-in library to communicate with SQLite

-- SQLite Docs: https://www.sqlite.org/index.html
-- - Datatypes in SQLite: https://www.sqlite.org/datatype3.html
-- - storage classes for datatypes are really only: null, integer, real (floats), text, and blob; see the documentation.
-- - there's no storage class for boolean datatypes; instead boolean values are stored as integers 0 (false) and 1 (true); see the documentation.
-- - there's no storage class for date and time datatypes; see the documentation.

-- open sql with command in terminal: "sqlite3"
-- Create/Open db file with: .open filename.db (ie. ".open cats_db.db")
-- After opening db file create table (see below) and paste into terminal.  Table is now saved in cats_db.db file.

-- Syntax to define a table:
CREATE TABLE cats(
    name TEXT,
    breed TEXT,
    age INTEGER
);

CREATE TABLE dogs(
    name TEXT,
    breed TEXT,
    age INTEGER
);

-- Adding to table (directly in command line):
INSERT INTO cats (name, breed, age) VALUES ("Buddy", "American Short Hair", 11);

-- Adding multiple values to table by reading a file:
-- - create insert into commands in file (see basics.sql file)
-- run in command line: ".read basics.sql" (this command read and inserted into dogs table from basics.sql file using ".read basics.sql")

-- Viewing all data in table:
SELECT * FROM cats;  -- returns the entire db

-- Viewing just one item in db:
SELECT * FROM dogs WHERE name IS "Piggy";  -- returns matching name with all column inputs
SELECT * FROM dogs WHERE breed IS "Husky";  -- returns matching breed with all column inputs
SELECT name FROM dogs WHERE breed IS "Husky";  -- returns matching breed with only name input
SELECT * FROM dogs WHERE breed IS NOT "Chihuahua";  -- returns matching breed that are NOT Chiuahua with all column inputs
SELECT * FROM dogs WHERE breed IS NOT "Chihuahua" AND breed IS NOT "Pug";  -- returns matching breed that are NOT Chiuahua/Pug with all column inputs
SELECT * FROM dogs WHERE age > 8;  -- returns matching age with all inputs
SELECT * FROM dogs WHERE name LIKE "%gg%";  -- returns matching names that have characters "gg" with all inputs
-- --------------------------------------------------------------------------

