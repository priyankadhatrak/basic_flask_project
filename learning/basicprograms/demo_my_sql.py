import mysql.connector

mydb = mysql.connector.connect (
    host="localhost",
    user="root",
    password="",
    database="priyanka"
    )

mycursor = mydb.cursor()
sql = "select * from Employee Limit 7 offset 2"


mycursor.execute(sql)
#mydb.commit()
res=mycursor.fetchall()
for x in res:
    print(x)