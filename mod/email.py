import re
# print(help(re.search))
# text = """
# """
inpu1 = input("Enter e-mail:")
# alp = 
val = re.search("^@gmail.com$",inpu1)
print(val)
if val:
    print("Welcome")
else:
    print("error")