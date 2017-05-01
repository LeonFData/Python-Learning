import sqlite3
#import urllib.request

#Connecting to the file in which we want to store our db
connetion = sqlite3.connect('emaildb1.sqlite')
cur = connetion.cursor()

#Deleting any possible table that may affect this assignment
cur.execute('''DROP TABLE IF EXISTS Counts''')

#Creating the table we're going to use
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

##url = 'http://www.pythonlearn.com/code/mbox.txt'
##page = urllib.request.urlopen(url).read().decode('utf8')

f = open('mbox.txt')
for line in f:
    if not line.startswith('From: '):
        continue
    email = line.split()[1]
    org = email.split('@')[-1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
        VALUES ( ?, 1 )''', (org, ) )
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (org, ))
    connetion.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print('Counts: ')
for row in cur.execute(sqlstr): print(str(row[0]), row[1])

cur.close()
          

