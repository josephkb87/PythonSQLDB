import mysql.connector

##create a connection to the database
con = mysql.connector.connect(host='localhost',database='mysql',user ='root',password='12345Trial1@')

#execute query
cur.execute(sql)
con.close()

#create database TABLE
sql = """CREATE TABLE EMPLOYEEZ(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT )"""


#print a statement
print('Database TABLE Successfully')




