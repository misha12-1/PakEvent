from flask import Flask,render_template , request
from flask_mysqldb import MySQL , MySQLdb


app= Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'flaskdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route("/")
def home():
   return render_template('home.html')
@app.route("/event")
def event():
   return render_template('event.html')
@app.route("/birthday")
def birthday():
   return render_template('birthday.html')
@app.route("/birthdayslider")
def birthdayslider():
   return render_template('birthdayslider.html')
@app.route("/package")
def package():
   return render_template('package.html')
@app.route("/wedding")
def wedding():
   return render_template('wedding.html')
@app.route("/weddingslider")
def weddingslider():
   return render_template('weddingslider.html')
@app.route("/gallery")
def gallery():
   return render_template('gallery.html')
@app.route("/contact")
def contact():
   return render_template('contact.html')
@app.route("/about")
def about():
   return render_template('about.html')
@app.route("/LoGIn" , methods = ["POST" , "GET"])
def login():
   if request.method == "GET":
      return render_template('LoGIn.html')
@app.route("/booking")
def booking():
   return render_template('booking.html')

@app.route("/registration" , methods = ["POST"])
def registration():
   name = request.form['username']
   email = request.form['email']
   password = request.form['pass']

   cur = mysql.connection.cursor()
   cur.execute("INSERT INTO register (name, email, password) VALUES (%s,%s,%s)", (name, email, password))
   mysql.connection.commit()
   return render_template('LoGIn.html')

@app.route("/login_model" , methods = ["POST"])
def login_model():
   email = request.form['email']
   return render_template('home.html')

app.run()

