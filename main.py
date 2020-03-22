import sqlite3
from flask import Flask, render_template
from flask import request
import pandas as pd
import bcrypt
from jinja2 import escape
from jinja2 import Markup

class City:
    def __init__(self, name, state, population):
        self.name = name
        self.state = state
        self.population = population


app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/handle_date', methods=['POST']) #'/test.py'
def handle_data():
    projectpath = request.form['projectFilepath']
    conn = sqlite3.connect('citiesDatabase.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM cities WHERE name = '%s'" % projectpath)
    
    #val = (projectpath,) #good one
    #c.execute('INSERT INTO cities (name, state, population) VALUES (?, "STATE", 0)', val)
    #c.execute('SELECT * FROM cities WHERE name = ?', val) #good one
    stash = []
    for row in c.fetchall():
      name = row[0]
      state = row[1]
      population = row[2]
      if name != "SecretCity":
        curr = City(name, state, population)
        stash.append(curr)
    #conn.commit()
    return render_template('home.html', stash=stash)
@app.route('/handle_date2', methods=['POST']) 
def handle_data2():
    projectpathC = request.form['projectFilepathC']
    projectpathS = request.form['projectFilepathS']
    projectpathP = request.form['projectFilepathP']
    conn = sqlite3.connect('citiesDatabase.db')
    c = conn.cursor()
    val = (projectpathC, projectpathS, projectpathP,)
    c.execute('INSERT INTO cities (name, state, population) VALUES (?, ?, ?)', val)
    conn.commit()
    return render_template('home.html')
    
@app.route("/handle_data3" , methods=['GET', 'POST'])
def handle_data3():
    select = request.form.get('DropDown')
    if select == "A":
        message = "Address: 123 Apple Blossem Avenue, City 1, State of Confusion 45678"
    elif select == "B":
        message = "Address: 456 Beautiful Butterfly Boulevard, City 1, State of Confusion 78910"
    elif select == "C":
        message = "Address: 789 Camelia Countess Court, City 1, State of Confusion 10111"
    elif select == "D":
        message = "Address: 213 Dusty Dragon Drive, City 1, State of Confusion 14151"
    elif select == "E":
        message = "Address: 617 Red River Road, City 1, State of Confusion 18192"
    elif select == "F":
        message = "Address: 021 Winter Sparks Way, City 1, State of Confusion 22232"
    else:
        message = "Not a Building"
    return render_template('home.html', message=message)
    #return(str(select)) # just to see what select is
    
@app.route("/handle_data4" , methods=['GET', 'POST'])
def handle_data4():
    userType = request.args.get('userType')
    #userType = request.form.get('adminbutton')
    if userType == "WVdSdGFXND0=":
        #admin user
        message2 = "The tresure is located in Building F."
    else:
        message2 = "Unable to access data. You are not an admin."
    return render_template('home.html', message2=message2)
    
@app.route('/handle_dataB', methods=['POST'])
def handle_dataB():
    projectpath = request.form['projectFilepath']
    conn = sqlite3.connect('citiesDatabase.db')
    c = conn.cursor()
    val = (projectpath,) #good one
    c.execute('SELECT * FROM cities WHERE name = ?', val) #good one
    print c.fetchall()
    stash = []
    for row in c.fetchall():
      name = row[0]
      state = row[1]
      population = row[2]
      curr = City(name, state, population)
      stash.append(curr)
    #conn.commit()
    return render_template('home.html', stash=stash)   
    
    
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    uniUser = username.encode('utf-8')
    uniPass = password.encode('utf-8')
    hashedU = bcrypt.hashpw(uniUser, bcrypt.gensalt())
    hashedP = bcrypt.hashpw(uniPass, bcrypt.gensalt())
    
    #testP = b"hellopassword"
    #hashed = bcrypt.hashpw(testP, bcrypt.gensalt())
    #if bcrypt.checkpw(testP, hashed):
        #print("It Matches!")
    #else:
   #     print("It Does not Match :(")

    conn = sqlite3.connect('accountsDatabase.db')
    c = conn.cursor()
    c.execute("SELECT * FROM accounts")
    message = 'incorrect username or password';
    for row in c.fetchall():
      userN = row[0]
      passW = row[1]
      userN = userN.encode('utf-8')
      passW = passW.encode('utf-8')
      if bcrypt.checkpw(uniUser, userN) and bcrypt.checkpw(uniPass, passW): #userN == username and passW == password:
        return render_template('decide.html')
    return render_template('index.html', message=message)
@app.route('/create_account', methods=['POST'])
def create_account():
    username = request.form['username']
    password = request.form['password']
    uniUser = username.encode('utf-8')
    uniPass = password.encode('utf-8')
    hashedU = bcrypt.hashpw(uniUser, bcrypt.gensalt())
    hashedP = bcrypt.hashpw(uniPass, bcrypt.gensalt())
    #to decode/check match: bcrypt.checkpw(uniUser, hashedU), if true, then match
    conn = sqlite3.connect('accountsDatabase.db')
    c = conn.cursor()
    val = (hashedU, hashedP,)
    c.execute('INSERT INTO accounts (username, password) VALUES (?, ?)', val)
    conn.commit()  
    return render_template('index.html')
@app.route('/redirect', methods=['POST'])
def redirect():
    return render_template('createAccount.html')
    
@app.route('/decide_good')
def decide_good():
    return render_template('betterHome.html')
    
@app.route('/decide_bad')
def decide_bad():
    return render_template('home.html')
    
if __name__ =='__main__':
	app.run(debug=True)
    
    
