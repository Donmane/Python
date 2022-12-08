
# Python Database (Mysql)
# To download mysql connector user: pip install mysql-connector
import mysql.connector
mycon = mysql.connector.connect(host='127.0.0.1', user='root', passwd='', database='cbtTest')

mycursor = mycon.cursor()

# mycursor.execute("CREATE DATABASE cbtTest")
# mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)

# mycursor.execute("CREATE TABLE customers (ctm_id INT(4), Ful_Name VARCHAR(20), Address VARCHAR(50), Phone VARCHAR(11), Password VARCHAR(20))")
# mycursor.execute("SHOW TABLES")

# for table in mycursor: 
#     print(table)

# mycursor.execute("ALTER TABLE customers CHANGE ctm_id ctm_id INT(4) PRIMARY KEY AUTO_INCREMENT")
# mycursor.execute("ALTER TABLE customers ADD UNIQUE(Phone);")
print("Fill in your details")
fulname = input('Enter your fullname >') 
address = input('Enter your Address ')
phone = input('Enter your phone number')
mothers = input('Enter your Mothers Maiden Name')
Salary = input('Enter your Montly Salary')
gender = input('Enter your Gender')
marital = input('Enter your Marital Status')
E_mail = input('Enter your E-mail')
password = input('Enter your passsword')
myquery = "INSERT INTO customerss (FullName, Address, Phone,MothersMaidenName,MontlySalary,Gender,MaritalStatus,E_mail, Password) VALUES(%s, %s, %s, %s,%s,%s,%s,%s,%s)"
val = (fulname, address, phone,mothers,Salary,gender,marital,E_mail, password)
mycursor.execute(myquery, val)
# mycursor.executemany((myquery, val),(),())
mycon.commit()
print(mycursor.rowcount, "records inserted successfully")
