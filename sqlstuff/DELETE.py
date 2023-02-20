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
#
# # Execute a command: this creates a new table
# #cur.execute('DROP TABLE IF EXISTS books;')
#
cur.execute('DROP TABLE  USERS;')
#
cur.execute('DROP TABLE  REQUESTS;')


conn.commit()

cur.close()
conn.close()