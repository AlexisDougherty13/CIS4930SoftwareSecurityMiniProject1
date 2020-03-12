import sqlite3
from flask import Flask, render_template
from flask import request
import pandas as pd

class City:
    def __init__(self, name, state, population):
        self.name = name
        self.state = state
        self.population = population


app=Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")
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
    
if __name__ =='__main__':
	app.run(debug=True)
    
    
