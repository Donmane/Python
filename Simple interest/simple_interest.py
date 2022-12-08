sim = "To calculate Simple interest"
print(sim)
pri = int(input("Enter the value for principal :"))
rate = int(input('Enter the value for rate :'))
time = int(input('Enter the value for time'))
cal = (pri * rate * time)/100
print('Simple interest :',f"${cal}")

tim = "To calculate  principal"
rim = int(input('Enter the value for interest :'))
rate = int(input('Enter the value for rate :'))
time = int(input('Enter the value for time:'))
sal = (rim)/rate * time
print('Principal:',f"${sal}")

tim = "To calculate Rate"
wim = int(input('Enter the value for interest :'))
qim = int(input("Enter the value for principal :"))
eim = int(input('Enter the value for time:'))
lal= (wim)/qim * eim
print('Rate:',f"%{lal}")

pim = "To calculate Time"
wim = int(input('Enter the value for interest :'))
qim = int(input("Enter the value for principal :"))
rate = int(input('Enter the value for rate :'))
rot = (wim)/qim * rate 
print('Time :'f"{wim}years")