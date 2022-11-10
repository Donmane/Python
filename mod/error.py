n = int(input("Enter nun :"))
try:
    if n == 8:
        print(n/0/m)
    else:
        print(8)
except ZeroDivisionError:
    print("Zero error")
except NameError:
    print("name error")
except SyntaxError:
    print("Syntax error")
finally:
    print("All good")