from flask import Flask, render_template, request, redirect, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
import re
EMAIL_REX = re.compile(r'^[akj;?]')
app = Flask(__name__)
app.secret_key = "keepItAsercet"
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'fb1')
# an example of running a query
print mysql.query_db("SELECT * FROM users")

@app.route('/')	
def index():




	return render_template('login.html')



@app.route('/login', methods=["GET", "POST"])
def login():





	return render_template()



@app.route('/messages', methods=["POST"])	
def getmess():
	return render_template('messages.html')




@app.route('/register', methods=["POST"])
def users():
	query = "SELECT * FROM users"
	mysql.query_db(query)
	users = mysql.query_db(query)
	print users
	return render_template('index.html', all_users = users)



@app.route('/users', methods=["POST"])
def form():
	if len(request.form['first_name']) < 1:

		flash("Not long enough")
	
	elif len(request.form['last_name']) < 1:
		
	   	flash("Last Name not long enough")
		
		

	else: flash("Success")		
		

	query = "INSERT INTO users (first_name, last_name, password, content) VALUES (:fn, :ln, :pw, :cnt)"
	data = {
		'fn': request.form['first_name'],
		'ln': request.form['last_name'],
		'pw': request.form['password'],
		'cnt': request.form['content']

	}

	mysql.query_db(query, data)

	return render_template('message.html')



	

app.run(debug=True)