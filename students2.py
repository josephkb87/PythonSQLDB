import mysql.connector

print("Content-Type: text/html;charset=utf-8")

print()
##create a connection to the database
con = mysql.connector.connect(host='localhost',database='studentw',user ='root',password='12345Trial1@')

#create a cursor#
cur = con.cursor()

#create insert statement
sql = "INSERT INTO EMPLOYEERED(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)"\
      "VALUES ('Mamiliaa','Johns','28','M', 7000)"\
      
sql = "INSERT INTO EMPLOYEEZ(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)"\
      "VALUES ('Justus','Reagan','25','M', 4000)"\
      
sql = "INSERT INTO EMPLOYEED(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)"\
      "VALUES ('Joseph','Right','32','M', 3800)"\

#execute query
cur.execute(sql)
con.close()


#print a statement
print('Database inserted Successfully')

import sys
if con.is_connected():
    print ('Connected to MySQL database')
    cursor.excute(""" SELECT * FROM EMPLOYEERED""")

# fetch all of the rows from the query
data = cur.fetchall ()

# print the rows
for row in data :
    print(row[1])
                  


