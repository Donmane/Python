val = input('Enter what you wnt to convert from :')
val1 = input('Enter what you want to convert to  :')
val3 = int(input("Enter no :"))
if (val == 'c') and (val1 == 'f') or (val == 'C') and (val1 == 'F'):
  cen = (val3 * 9/5) + 32 
  print(cen ,'F')

if (val == 'f') and (val1 == 'c') or (val == 'F') and (val1 == 'C'):
  cen = (val3 - 32) * 5/9
  print( cen,'C')

if (val == 'c') and (val1 == 'k') or (val == 'C') and (val1 == 'K'):
  cen = val3 + 273.15
  print(cen,'K')

if (val == 'f') and (val1 == 'k') or (val == 'F') and (val1 == 'K'):
  cen = (val3 - 32) * 5/9 + 273.15
  print(cen,'K')

if (val == 'k') and (val1 == 'c') or (val == 'K') and (val1 == 'C'):
  cen = val3 - 273.15
  print(cen,'C')

if (val == 'k') and (val1 == 'f') or (val == 'K') and (val1 == 'F'):
  cen = (val3 - 273.15) * 9/5 + 32
  print(cen,'F')

          
          