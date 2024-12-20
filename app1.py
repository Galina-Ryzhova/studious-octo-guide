from flask import Flask, render_template
import sqlite3 as sl
app = Flask(__name__) 
@app.route('/')
def index1(): 
    conn = sl.connect('my_kinozal.db') 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM my_films") 
    data = cursor.fetchall() 
    conn.close() 
    return render_template('index1.html', data=data)