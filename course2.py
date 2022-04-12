import mysql.connector

#create a connection to the database
con = mysql.connector.connect(host ='localhost',database ='mysql',user='root',password='12345Trial1@')

#create a cursor
cur = con.cursor()

#execute query
cur.execute('CREATE DATABASE school')

#print a statement
print('Database Created Successfully')
