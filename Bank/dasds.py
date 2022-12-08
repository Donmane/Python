import mysql.connector
mycon = mysql.connector.connect(host='127.0.0.1', user='root', passwd='', database='Banks')

mycursor = mycon.cursor()


# mycursor.execute("CREATE DATABASE cbtTest")
# mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)
