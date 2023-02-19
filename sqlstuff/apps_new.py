from pprint import pprint
import requests
import json
import sys
import os
import psycopg2

#try:
from flask import Flask
from flask import request
#except Importerror as e:
 #   print(e)
  #  print("Looks like 'flask' library is missing.\n"
   #       "type pip3 install flask command to install the missing library.")
    #sys.exit()

app = Flask(__name__)
username='postgres'
pw='5240Young'


# Open a cursor to perform database operations

@app.route('/')
@app.route('/index',methods=['GET','POST'])

def index():
    if request.method=='POST':

        req=request.get_json(silent=True)

        print(req)

        con = psycopg2.connect(
            host="localhost",
            database="flask_db",
            user=username,  # os.environ['DB_USERNAME'],
            password=pw)  # os.environ['DB_PASSWORD'])
        cur = con.cursor()
        cur.execute('INSERT INTO  REQUESTS ( id, Name,Password,Address,Number ,Email,Emergency_Contact,Age,'
                    'Gender,Status,Comment,lat,long)'
                    'VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s,%s, %s, %s, %s)', (
                                                                                 req['id'],req['Name'],req['Password'],
            req['Address'],req['Number'],req["Email"],req["Emergency_Contact"],req["Age"],
                    req["Gender"],req["Status"],req["Comment"],req["lat"],req["long"])
                    )

        con.commit()

        cur.close()
        con.close()
        #
    return "hello"
def main():
    app.run(host='localhost', port=8080)
if __name__=="__main__" :
	main()

