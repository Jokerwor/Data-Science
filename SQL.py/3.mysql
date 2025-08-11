
import mysql.connector 
from mysql.connector import Error


mydb = mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password"
)

print(mydb)

mycursor = mydb.cursor()
mycursor.execute("select : from test1.test_table")

for x in mycursor.fetchall:
    print(x)

mydb.close()