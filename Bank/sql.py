import random
import re
import os
import mysql.connector
mycon = mysql.connector.connect(host='127.0.0.1', user='root', passwd='', database='level_one_project')
mycursor = mycon.cursor()

class sql:
    def __init__(self):
        self.regg()

    def regg(self): 
        fulname = input('Enter your fullname:') 
        address = input('Enter your Address: ')
        phone = (input('Enter your phone number:'))
        myphone = phone
        if (len(myphone)) == (11):
          pass
        else:
          print("Invalid number")
          quit()
        if (phone).startswith('08'):
            pass
        else:
            print("Invalid Phone Number")
            quit()

        mothers = input('Enter your Mothers Maiden Name:')
        Account_Balnce = int(input('Enter your Montly Account_Balnce: $'))
        gender = input('Enter your Gender:')
        marital = input('Enter your Marital Status:')
        E_mail = input('Enter your E-mail:')
        val = re.search("@gmail.com$",E_mail)
        
        if val:
         pass 
        else:
         print("Invalid Email")
         quit()
        Password = input('Enter your passsword:')     
        credit = ""
        debit = ""
        Account_Number =  "01" + str(random.randint(10000000 , 50000000))
        myquery = "INSERT INTO customers (Ful_Name, Address, Phone,Mothers,Account_Balnce,Gender,Martial,Email, Password,Credit,Debit,Account_Number) VALUES(%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (fulname, address, phone,mothers,Account_Balnce,gender,marital,E_mail, Password,credit,debit,Account_Number)
        mycursor.execute(myquery, val)
        mycon.commit()
        mycursor.execute("ALTER TABLE customers ADD UNIQUE(Email);")
        youraccount = Account_Balnce
        print(f"Your account number is {youraccount}")
        print(mycursor.rowcount, "records inserted successfully")
        print("")
        print("")
        print(f"Welcome Mr {fulname} which bank would you like to register for")
        print("1. First Bank\n2.GT Bank\n3.Wema Bank\n4.Zenith Bank\n5.Access Bank")

    def gt(self):
        print()
        print("What can we do for you")
        print("1. Quick Balance\n2.Quick transfer\n3.Quick Airtime\n4.Soft Token\n5.Contact account manager")
        inp3 = input("Enter:")
        if inp3 == "1":
            query = "Select Account_Balnce from customers where Email = %s AND Password=%s"
            emai = input("Enter your email here:")
            va = re.search("@gmail.com$",emai)
            if va:
               pass 
            else:
              print("Invalid Email")
              quit()
            pin = input("Enter your pin here:")
            val = (emai,pin) 
            mycursor.execute(query,val)
            myreg = mycursor.fetchone()
            mycon.commit()
            print(f"You currently have ${myreg[0]} in your account")

        elif inp3 == "2":
            print("Quick Transfer Limit:$ 50000\n  Cumulative Daily Limit:$ 1,500")                
            print("Amount")
            inp9 = int(input("Enter Amount:$"))
            print("Benifactor")
            inp22 = input("Enter Benifactor's name:") 
            print("Mobile Number")
            inp0 = int(input("Enter:"))
            myphone = str(inp0)
            if (len(myphone)) == (10):
              pass
            else:
              print("Invalid number")
              quit()
            if str(inp0).startswith('8'):
              pass
            else:
              print("Invalid Phone Number")
              quit()
            query = "Select Account_Balnce from customers where Email = %s AND Password=%s"
            emai = input("Enter your email here:")
            va = re.search("@gmail.com$",emai)
            if va:
               pass 
            else:
              print("Invalid Email")
              quit()
            pin = input("Enter your pin here:")
            vop = (emai,pin) 
            mycursor.execute(query,vop)
            myreg = mycursor.fetchone()
            mycon.commit()
            quen = ("UPDATE customers SET Account_Balnce = %s where Password = %s ")
            datatrans = myreg[0] - inp9
            # password = int(input("enter:"))
            data = (datatrans,pin)
            mycursor.execute(quen,data)
            mycon.commit() 
            print(F"Transfer successful ${inp9} has been transferred to {inp22}")

        elif inp3 == "3":
            print("Quick Airtime Transaction Limit:$ 500\n  Cumulative Daily Limit:$ 1,500")    
            print("  Select Category\n1.Buy Data \n2.Airtime")
            inp7 = input("Enter:")
            print("Select a network\n1.Glo\n2.Airtel\n3.Mtn\n4.9mobile")    
            inp8 = input("Enter")
            print("Amount")
            inp9 = int(input("Enter Amount:$"))
            print("Mobile Number")
            inp0 = int(input("Enter:"))
            myphone = str(inp0)
            if (len(myphone)) == (10):
              pass
            else:
              print("Invalid number")
              quit()
          
            if str(inp0).startswith('8'):
              pass
            else:
              print("Invalid Phone Number")
              quit()
            query = "Select Account_Balnce from customers where Email = %s AND Password=%s"
            eemai = input("Enter your email here:")
            va = re.search("@gmail.com$",eemai)
            if va:
               pass 
            else:
              print("Invalid Email")
              quit()
            pin = input("Enter your pin here:")
            vol = (eemai,pin) 
            mycursor.execute(query,vol)
            myreg = mycursor.fetchone()
            mycon.commit()
            quen = ("UPDATE customers SET Account_Balnce = %s where Password = %s ")
            datatrans = myreg[0] - inp9
            password = int(input("enter:"))
            data = (datatrans,password)
            mycursor.execute(quen,data)
            mycon.commit()
            print(F"Transfer successful ${inp9} has been debited from account")
        elif inp3 == "4":
            print("____Soft Token____\nSoft Token will expire in 15 minutes")
            ran = str(random.randint(100000,500000))
            print(ran)
        elif inp3 == "5":
            print("Manager Is Currently Unavailable")
        print("Is there anything you still wish to do?")
        inpu1 = input("Enter:")
        if inpu1 == "yes":
            print(self.gt())
        else:
            quit()