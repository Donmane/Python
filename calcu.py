inpu1 = int(input('input number :'))
inpu2 = int(input('input number :'))
def calcu():
 for k in range(1,inpu1):
    for i in range(1,inpu2):
     cal = k * i  
     print(f"{k} x {i} = {cal}")
calcu()