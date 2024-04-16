#How to install this
#py -m install virtualenv
#py -m virtualenv env
#env\Scripts\activate.ps1
#py -m pip install flask
#py -m pip install mysq-connector
#py -m install mysql-connector-python

#How to connect to the sql server
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd="Word.12345",
#    database = "testdatabes" Database has not been created yet
)

mycursor = db.cursor()

#Creates the database 
mycursor.execute("CREATE DATABASE testdatebes")
"""
#How to add or create information
mycursor.execute("CREAT TABLE Person(name VARCHAR(50), age smallint unsigned, personID int Primary key Auto_Increment)")

mycursor.execute("DESCRIBE Person")

mycursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)",("Tim","19"))
db.commit()

for x in mycursor:
    print(x)

