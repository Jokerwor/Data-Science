
import mysql.connector 
from mysql.connector import Error


mydb = mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password"
)

print(mydb)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

# Close cursor and connection when done
mycursor.close()
mydb.close()