#  Structured Query Language (SQL)

## What is a database?
* A database is a file that is organized for storing data. Most databases are organized like a dictionary in the sense that they map from keys to values.
* In technical descriptions of relational databases the concepts of table, row, and column are more formally referred to as relation, tuple, and attribute, respectively.

## Types of database
* Oracle
* MySQL
* Microsoft SQL Server
* PostgreSQL
* SQLite 

> [Github SQLite](https://github.com/sqlitebrowser)
> [Download SQLite](https://sqlitebrowser.org/dl/#windows)


## CRUD
* **Create:**
  * CREATE TABLE "Users" ("name" TEXT, "email" TEXT)
  * INSERT INTO Users (name, email) VALUES ('Chuck', 'csev@umich.edu')

* **Read:**
  * SELECT * FROM Users
  * SELECT * FROM Users WHERE email='csev@umich.edu'
  * SELECT * FROM Users ORDER BY email
  * SELECT * FROM Users ORDER BY name DESC 

* **Update:**
  * UPDATE Users SET name="Charles" WHERE email='csev@umich.edu'
    
* **Delete:**
  * DELETE FROM Users WHERE email='ted@umich.edu'  
