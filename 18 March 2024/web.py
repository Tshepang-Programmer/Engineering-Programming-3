from flask import Flask, render_template, request
import sqlite3
import os

currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route("/")
def signup():
    return render_template("index.html")

@app.route("/", METHODS = ['POST', 'GET'])
def home():
    my_name = request.form["email"]
    my_pass = request.form["psw"]
    connection = sqlite3.connect(currentdirectory + "\week5db.db")
    cur = connection.cursor()
    cur.execute("insert into customer(Customer_name, Customer_Pass) Values (?,?)", (my_name, my_pass) )
    connection.commit()


    return render_template("index.html")

if __name__ == "main":
    app.run(debug=True)

