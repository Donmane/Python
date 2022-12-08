firstno = int(input("Enter num :"))
even = []
odd = []
prime = []
for k in range(1,13):
    col = firstno * k
    calk = f'{firstno} x {k} = {firstno * k} '
    print(calk)
    if (col % 2 == 0):
     even.append(col) 
    else:
        odd.append(col)
    n = 0
print(f"Even numbers = {even}")
print(f"Odd numbers = {odd}")