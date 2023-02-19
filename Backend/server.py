# Import flask and datetime module for showing date and time
import psycopg2
from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify, abort
import datetime
from flask_cors import CORS, cross_origin


x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)
CORS(app, support_credentials=True)

# Route for seeing a data
@app.route('/data')
def get_time():
	# Returning an api for showing in reactjs
	return jsonify({
		'Name':"geek",
		"Age":"22",
	    "Date":x,
	    "programming":"python"
    })
########
@app.route('/main', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def get_user_info():
	if request.method == "GET":
		print("GET method")
		return "Main page...(pending)"
	if request.method == "POST":
		print("POST method")
		req=request.get_json(silent=True)
		print(request.get_json()["password"])
		print(request.get_json()["userEmail"])



		user = 'postgres'
		pw = 'vamsi'

		conn = psycopg2.connect(
		host="localhost",
		database="flask_db",
		user=user,  # os.environ['DB_USERNAME'],
			 		password=pw)  # os.environ['DB_PASSWORD'])
		print("here")
	# Open a cursor to perform database operations
		cur = conn.cursor()
		print("type!!!")
		print(type(req['userEmail']))
		cur.execute('INSERT INTO  LOGINS(Email) VALUES (%s)',(req['userEmail'],))

		print("here2")
		conn.commit()

		cur.close()
		conn.close()
		return "help"
#
# Running app
if __name__ == '__main__':
	app.run(debug=True)
