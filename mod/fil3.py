from fil1 import mymath as mt
mtm =mt()
def allmath():
    print("_______welcome to paul math function calculation_______") 
    print("1. ADDITION\n2.SUB\n3. MUL\n4. DIV\n 5.Modulus\n6. Square root\n7.Exponential\n8. Factorial\n9.Permutation\n10. Combination")
    ask = input("Enter any calculation of your choice here:")

    if ask == "1":
        first = int(input("Enter your value here:"))
        second = int(input("Enter your value here:"))
        print(mtm.add(first,second))

    elif ask == '2':
        first = int(input("Enter your value here:"))
        second = int(input("Enter your value here:"))
        print(mtm.sub(first,second))

    elif ask == '3':
        first = int(input("Enter your value here:"))
        second = int(input("Enter your value here:"))
        print(mtm.mul(first,second))

    elif ask == '4':
        first = int(input("Enter your value here:"))
        second = int(input("Enter your value here:"))
        print(mtm.div(first,second))

    elif ask == '5':
        first = int(input("Enter your value here:"))
        second = int(input("Enter your value here:"))
        print(mtm.mol(first,second))

    elif ask == '6':
        first = int(input("Enter your value here:"))
        print(mtm.sqr(first))

    elif ask == '7':
        first = int(input("Enter your value here:"))
        second = int(input("Enter your value here:"))
        print(mtm.exp(first,second))

    elif ask == '8':
        first = int(input("Enter your value here:"))
        print(mtm.paul(first))

    elif ask == '10':
        first = int(input("Enter your value here:"))
        second = int(input("Enter your value here:"))
        print(mtm.com(first,second))
       

allmath()