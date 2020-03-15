import sqlite3
from flask import Flask, render_template
from flask import request
import pandas as pd
import bcrypt

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
        return render_template('home.html')
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
    
if __name__ =='__main__':
	app.run(host="127.0.0.1",port=8080, debug=True)
