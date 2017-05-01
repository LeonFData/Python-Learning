'''
Instructions
If you don't already have it, install the SQLite Browser from http://sqlitebrowser.org/.

Then, create a SQLITE database or use an existing database and create a table in the database called "Ages":

CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)
Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only these rows with the following commands:

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Tracy', 28);
INSERT INTO Ages (name, age) VALUES ('Mikayla', 22);
INSERT INTO Ages (name, age) VALUES ('Shakeira', 40);
INSERT INTO Ages (name, age) VALUES ('Asim', 18);

Once the inserts are done, run the following SQL command:
SELECT hex(name || age) AS X FROM Ages ORDER BY X
Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333.

Note: This assignment must be done using SQLite - in particular, the SELECT query above will not work in any other database.
So you cannot use MySQL or Oracle for this assignment.
'''

import sqlite3

conn = sqlite3.connect('organization.sqlite')
cur = conn.cursor()

cur.executescript('''CREATE TABLE Ages(name VARCHAR(128), age INTEGER);
               DELETE FROM Ages;
               INSERT INTO Ages(name, age) VALUES('Tracy', 28);
               INSERT INTO Ages(name, age) VALUES('Mike', 22);
               INSERT INTO Ages(name, age) VALUES('Tommy', 40);
               INSERT INTO Ages(name, age) VALUES('Gary', 18);
               ''')
