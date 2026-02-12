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
  ```sql
  * CREATE TABLE "Users" ("name" TEXT, "email" TEXT)
  * INSERT INTO Users (name, email) VALUES ('Chuck', 'csev@umich.edu') 
   ```
  
* **Read:**
  ```sql
  * SELECT * FROM Users
  * SELECT * FROM Users WHERE email='csev@umich.edu'
  * SELECT * FROM Users ORDER BY email
  * SELECT * FROM Users ORDER BY name DESC
  ```

* **Update:**
  ```sql
  * UPDATE Users SET name="Charles" WHERE email='csev@umich.edu'
  ```
    
* **Delete:**
  ```sql
  * DELETE FROM Users WHERE email='ted@umich.edu'
  ```  

---
## Relationships in a Database
* Database Normalization (3NF)
  * Do not replicate data - reference data - point data
  * Use integers for keys and for references
  * Add a special "key" column to each table which we will make references to. (column "id")
 * We use integers to reference rows in another table

---
 
## Three Kinds of Keys
* **Primary key:** generally an integer auto-increment field
* **Logical key:** what the outside world uses for looking
* **Foreign key:** generally an integer key pointing to a row in another table

## Key Rules
* Best practices
  * Never use your logical key as the primary key
  * Logical keys can and do change, albeit slowly
  * Relationships that are based on matching string fields are less efficient than integers
 
## Foreign Keys
* A foreign key is when a table has a column that contains a key which points to the primary key of another table
* When all primary keys are integers, then all foreign keys are integers - this is very good)
---

---
# Multi-Table SQL:

```sql
CREATE TABLE "Artist" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    "name" TEXT)

CREATE TABLE "Album" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    artist_id INTEGER,
    "title" TEXT)

CREATE TABLE "Genre" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    "name" TEXT)

CREATE TABLE "Track" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    album_id INTEGER, genre_id INTEGER, len INTEGER, rating INTEGER, 
    "title" TEXT, "count" INTEGER)

INSERT INTO Artist (name) VALUES ('Led Zepplin')
INSERT INTO Artist (name) VALUES ('AC/DC')

INSERT INTO Genre (name) VALUES ('Rock') ;
INSERT INTO Genre (name) VALUES ('Metal');

INSERT INTO Album (title, artist_id) VALUES ('Who Made Who', 2);
INSERT INTO Album (title, artist_id) VALUES ('IV', 1);

INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Black Dog', 5, 297, 0, 2, 1) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Stairway', 5, 482, 0, 2, 1) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('About to Rock', 5, 313, 0, 1, 2) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Who Made Who', 5, 207, 0, 1, 2) ;
```

## The JOIN Operation
* The JOIN operation links across several tables as part of a select operation
* You must tell the JOIN how to use the keys that make the connection between the tables using an ON clause
* Joining two tables without an ON clause gives all possible combinations of rows

> What we want to see | The tables whoch hold the data | How the tables are linked

```sql
SELECT Album.title, Artist.name FROM Album JOIN Artist 
    ON Album.artist_id = Artist.id

SELECT Album.title, Album.artist_id, Artist.id, Artist.name 
    FROM Album JOIN Artist ON Album.artist_id = Artist.id

SELECT Track.title, Genre.name FROM Track JOIN Genre 
    ON Track.genre_id = Genre.id

SELECT Track.title, Artist.name, Album.title, Genre.name 
FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.id AND Track.album_id = Album.id 
    AND Album.artist_id = Artist.id
```



