from ussd1 import myussd as uss
ussd = uss()
print("Register")
reg1 = input("Enter name:")    
if reg1 == "":
 print("Input is empty")
 quit()
def wel():
     print(ussd.air())
     inpuda = input(">>>")
     if inpuda == "1":
        print(ussd.dai())
     elif inpuda == "2":
        print(ussd.wee())
     elif inpuda == "3":
        print(ussd.mon()) 
     elif inpuda == "4":
        print(ussd.bimonth())
     elif inpuda == "5":
        print(ussd.opera())
     elif inpuda == "6":
        print(ussd.opera())   
     elif inpuda == "7":
        print(ussd.insta())
     else:
        print("Does not compute")
        quit()   
     print("thanks for shopping") 
 
def us():
    print(f"welcome {reg1} which network do you want to use ")
    print("1 for Mtn\n2 for Airtel\n3 for Glo")
    inp1 = input(">>>")
    if inp1 == "1":
     print(f"_______welcome {reg1}______Mtn")
     
     print(wel())

    elif inp1 == "2":
     print(f"_______welcome {reg1}______Airtel")
     
     print(wel())

    elif inp1 == "3":
     print(f"_______welcome {reg1} to Glo______")
     
     print(wel())
us()