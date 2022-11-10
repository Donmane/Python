Welcome = "Welcome to my Mathematical Calculator..."
print(Welcome)

one = "(1) Additional" 
two = "(2) Subtraction"
three = "(3) Multiplication"
four = "(4) Expomential"
five = "(5) Factorial"
six = "(6) Combination"
print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
inpu = int(input("Enter your choice :"))

if inpu == 1 :
 inpu1 = int(input("Enter your number :"))
 inpu2 = int(input("Enter your number :"))
 sun =  inpu1 + inpu2
 print(sun)

if inpu == 2 :
 inpu1 = int(input("Enter your number :"))
 inpu2 = int(input("Enter your number :"))
 tom =  inpu1 - inpu2
 print(tom)

if inpu == 3 :
 inpu1 = int(input("Enter your number :"))
 inpu2 = int(input("Enter your number :"))
 bum =  inpu1 * inpu2
 print(bum)

if inpu == 4 :
  inpu1 = int(input("Enter your number :"))
  inpu2 = int(input("Enter your number :"))
  iol =  inpu1 ** inpu2
  print(iol)

if inpu == 5 :
   ono = int(input('Enter your number :'))
   fac  = 1
   for i in range(1, ono + 1 ):
    fac = fac * i
    print(fac)

if inpu == 6 :
    inpu1 = int(input("Total number of objects in the set :"))
    inpu2 = int(input("Number of choosing objects from the set:"))
    com = 1
    for i in range(1, inpu1 + 1 ):
     com = com * i

     com1 = 1
    for i in range(1, inpu1 + 1 ):
     com1 = com1 * i

    combine = (inpu1)/inpu2(inpu1 - inpu2)

    print(combine)