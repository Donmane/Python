num1 = int(input('Enter num :')) 
sign = input('Enter operator:')
num2 = int(input('Enter num :'))
def myfunction() :
 if sign == '+' :
  sun =  num1 + num2
  print(f'{num1} + {num2} = {sun}')
 
 elif sign == '-' :
  tom =  num1 - num2
  print(f'{num1} - {num2} = {tom}')

 elif sign == 'x' :
  bum =  num1 * num2
  print(f'{num1} x {num2} = {bum}')

 elif sign == '/' :
   iol =  num1 / num2
   print(f'{num1} / {num2} = {iol}')

 else:
    print('incorrect')
myfunction()

