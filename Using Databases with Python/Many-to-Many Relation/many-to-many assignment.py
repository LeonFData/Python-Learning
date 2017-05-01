import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# build tables
cur.executescript('''
drop table if exists User;
drop table if exists Member;
drop table if exists Course;

create table User(
    id Integer Not Null Primary Key Autoincrement Unique,
    name Text Unique);

create table Course(
    id Integer Not Null Primary Key Autoincrement Unique,
    title Text Unique);

create table Member(
    user_id Integer,
    course_id Integer,
    role Integer,
    Primary Key (course_id, user_id))
''')

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ]
#  ],

str_data = open('roster_data.json').read()
json_data = json.loads(str_data)

for item in json_data:
    name = item[0]
    title = item[1]
    role = item[2]
    print(name, title, role)

    cur.execute('insert or ignore into User(name) values(?)', (name, ))
    cur.execute('select id from User where name = ?', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('insert or ignore into Course(title) values(?)', (title, ))
    cur.execute('select id from Course where title = ?', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''insert or ignore into Member(user_id, course_id, role)
                        values(?, ?, ?)''', (user_id, course_id, role))
    conn.commit()
