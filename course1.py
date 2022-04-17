import mysql.connector

##create a connection to the database
con = mysql.connector.connect(host='localhost',database='school',user ='root',password='12345Trial1@')

#create a cursor#
cur = con.cursor()


sql = """CREATE TABLE EMPLOYEES(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT )"""

#execute query
cur.execute(sql)
con.close()

#print a statement
print('Database Created Successfully')

