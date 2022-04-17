import mysql.connector

##create a connection to the database
con = mysql.connector.connect(host='localhost',database='studentZ',user ='root',password='12345Trial1@')

#create a cursor#
cur = con.cursor()

cur.execute('CREATE DATABASE studentz1')

#print a statement
print('Database Created Successfully')



