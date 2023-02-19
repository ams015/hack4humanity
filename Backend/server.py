# Import flask and datetime module for showing date and time
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
@app.route('/main', methods=['POST'])
@cross_origin(supports_credentials=True)
def get_user_info():
		print("POST method")
		print(request.get_json()["password"])
		return redirect(url_for("http://127.0.0.1/main"))

@app.route('/main', methods=['GET'])
def show_main_page():
	print("GET method")
	return "Main page...(pending)"
	
# Running app
if __name__ == '__main__':
	app.run(debug=True)
