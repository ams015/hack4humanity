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

# Execute a command: this creates a new table
#cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('CREATE TABLE USERS (id serial PRIMARY KEY,'
                                 'Name varchar (50) NOT NULL,'
                                 'Password varchar (50) NOT NULL,'
                                 'Address varchar (50),'
                                 'Number varchar (10),'
                                 'Email varchar (150) NOT NULL,'
                                 'Emergency_Contact varchar (10),'
                                 'Age integer,'
                                 'Gender varchar(10),'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )
cur.execute('CREATE TABLE REQUESTS(id serial PRIMARY KEY,'
                                  'Name varchar(50) NOT NULL,'
                                  'Password varchar(50) NOT NULL,'
                                  'Address varchar(50) ,'
                                  'Number varchar(10),'
                                  'Email varchar(150) NOT NULL,'
                                  'Emergency_Contact varchar(10),'
                                  'Age integer,'
                                  'Gender varchar(10),'
                                  'Status varchar(30),'
                                  'Comment varchar(500),'
                                  'lat double precision,'
                                  'long double precision,'
                                  'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                  )
# Insert data into the table
#
# cur.execute('INSERT INTO books (title, author, pages_num, review)'
#             'VALUES (%s, %s, %s, %s)',
#             ('A Tale of Two Cities',
#              'Charles Dickens',
#              489,
#              'A great classic!')
#             )
#
#
# cur.execute('INSERT INTO books (title, author, pages_num, review)'
#             'VALUES (%s, %s, %s, %s)',
#             ('Anna Karenina',
#              'Leo Tolstoy',
#              864,
#              'Another great classic!')
#             )

conn.commit()

cur.close()
conn.close()