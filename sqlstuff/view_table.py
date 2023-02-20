import os
import psycopg2


user='postgres'
pw='vamsi'

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=user,#os.environ['DB_USERNAME'],
        password=pw)#os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()
cur.execute('select * from requests')
for table in cur.fetchall():
    print(table)

# Execute a command: this creates a new table
#cur.execute('DROP TABLE IF EXISTS books;')
a=cur.execute('select * from requests')
print(a)

conn.commit()

cur.close()
conn.close()