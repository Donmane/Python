# name = "daniel"
# val = str(10)
# print(val)
# print(type(val))
# print('i am' + val + 'years old')
# name = 'Mondays'
# print(name[-3:])
# name2 = "shade"
# print(name2)
# print(len(name2))
# print(type(name2))
# comment = """   commented that fr  km;g e
# f gepoigepimgi   """
# print(comment)
# print(len(comment))
# print(comment[-7:-3])
# print(comment.startswith('commented'))
# print(comment.endswith('i'))
# print('length before strip is' , len(comment))
# print('length before strip is' , len(comment.strip()))
# x = 10
# print("x is of type",type(x))

# y=10.6
# print("y is of type",type(y))
#  z = x + y
#  print(z)
#  print|("z is of type",type(z))
# x = 3
# name = 'weeks'
# # z = x + name
# print(x, name)
# val1 = int(input('How much dollars do you want to convert to naria: '))
# val2= int(input('enter value for val2: '))

# res =  val1 * 400  
# print(res , 'Naria')
# x = 5
# y = 7
# print(x==y)
# x = int(input('Enter value for x:'))
# y = int(input('Enter value for y:'))
# m = 0
# z = x % y
# print(z)
# print(z==m)
# x = 5
# x *= 5
# print(x)
# x = 5
# x += 5
# print(x)
# x = 5
# x /= 5
# print(int(x))
# x = 5
# x //= 5
# print(x)
# x = 10
# y = 20
# tot = (x != y) or (x >= y)
# print(tot)
# x = 15
# y = 15
# total = x is y
# print(total)
# x = 15
# y = 15
# total = x is not y
# print(total)

# one = [1,2,3,4,5,6,7,8,9]
# # two = 6
# # total = two in one
# # print(total)
# x = 780
# y = 54
# age = [6,7,4,3,6]
# agenum = ((6 not in age) and (10 in age) and (20 not in age) or (x == y))
# print(agenum)
# fruit = ['mango', 'banana', 'orange', 'pawpaw']
# out = 'banana'
# print(out in fruit)
# print(type(fruit))
# comment = """commented is python class, it started last
#  week and continue through this week. the number of people in this class is   """
# val = (input('which word do you want to chect :'))
# print(comment)
# print(val  in comment[22:74])
# print(comment[22:74].startswith(val))

# value = "login"
# user = input("please enter method to continue:")
# if value == user.upper():
#     print('Welcome')
#     else:
#          print('invalid')
# comment = """commented is python class, it started last
#  week and continue through this week. the number of people in this class is   """
# print(comment.split('.'))
# value = ["rice", "beans", "yam", "pot"]
# print(value)
# print(",".join(value))

# val1 = (input("Enter your name : "))
# val2 = (input("Number of students :"))
# val3 = (input("Enter word :"))
# comment = f"""{val1} commented that this is python class. it was started last week and continue this week
# the number of students are   {val2}"""

# print(comment.format(val1, val2).replace("python",val3))

# mylist = ["Shade", "Energy", "Lily", "Henry", "Josh"]
# val = (input("Enter word to append : "))
# # mylist.insert(-2, "tunde")
# mylist.append(val)
# print(mylist)
# num = int(input("Enter num :"))
# val2 = (input("Enter word to insert:"))
# mylist.insert(num, val2)
# print(mylist)

# if 12 in mylist:
#     print('present')
# else:
#     print('not available')
# mylist[1] = "Solar"
# print(mylist)
# print(mylist[1:3])
# for name in mylist:
#     print(name)
# comment = """commented that this is python class. it was started last week and continue this week
# the number of students are   """
# val1 = comment.split()
# val = input("Enter word to append : ")
# # # comment = comment + val
# val1.append(val)
# print(val1)
# num = int(input("Enter num :"))
# val2 = input("Enter word to insert:")
# val1.insert(num, val2)
# print(val1)
# print(comment.strip().split())

# comment = """commented that this is python class. it was started last week and continue this week
# the number of students are   """
# print(comment)
# val1 = comment.split()
# val = input("Enter sentence : ")
# sentence= val.split()
# print(sentence)
# val1.extend(sentence)
# print(val1)
# val2 = input("Enter word : ")

# if val2 in val1:
#     print("is available")
# else:
#     print("is not available")
# num = int(input("Enter num here:"))
# num2 = val1[num:num4]
# print(num2)
    #    POP
# fruit = ['mango', 'banana', 'orange', 'pawpaw']
# # del fruit[-1]
# print(fruit)
# num4 = int(input("Enter second number:"))
# fruits = fruit.pop(num4)
# print(fruits)
#     #    SORT
#     fruits = ['13', 'banana', 'orange', '2']
# fruit = fruits.sort()
# print(fruit)
    
    #    Unpacking values of a tuple
    
# (*name, ) = item
# print(name)
# item = ('yam','name', 'sunday','lagos','yam','sunday','lagos','45')
# print(item.index('name'))
# item = (|'yam','name', 'sunday','lagos','yam','sunday','lagos','45')
# print(max(item))
# mylist = [4,6,8,4,7]
# print(type(mylist))
# mylist = (4, 6, 8, 4, 7)
# print(type(mylist))
# name = {'yam','name', 'sunday','lagos','yam','sunday','lagos','45'}
# print(name)
# set1 = {1}
# set2 = {2,4,5,7,8,12,13}
# set3 = {20, 40, 60}
# # print(set3)
# # set1.update(set2)
# # print (set1)
# print('set1', set1)
# print('set2', set2)   
# print('set3', set3)
# item = ['yam','name', 'sunday','lagos','yam','sunday','lagos','45']
# print(item)
# print(type(item))
# item = ('yam','name', 'sunday','lagos','yam','sunday','lagos','45')
# print(item)
# print(type(item))
# item = {'yam','name', 'sunday','lagos','yam','sunday','lagos','45'}
# print(item)
# print(type(item))




# set2 = """commented that this is python class. it was started last week and continue this week
#  the number of students are   """

# val1 = set2.split()
# s = set(set2.split())
# print(s)
# val = input("Enter sentence : ")
# sentence= val.split()
# print(sentence)
# val1.extend(sentence)
# print(val1)
# val3 = (input("enter :"))
# inter = set(val3.split())
# setup = s.intersection(inter)
# print(setup)

# i = range(8)
# for n in i:
#  print(n)
# product = {'producers':'Toyota','model':'venza 2021','engine':'6 engine'
# ,'color':'black','gear':6,'ok':True}
# product["engine"] = "Lexus"
# # for x, y in product
# print(product)
# product.update({"Year":2023,"color":"white","speed":500})
# print(product)
# # product.popitem()
# # print(product)
# # del product['gear']
# # print(product)



# record = int(input('Enter no :'))
# for i in range(record):
#  josh = input('Enter full name:')
#  dsan = input('Enter level:') 
#  ichi = input('Enter your address:'),
#  sup = input('Enter your department:');  

#  product = {'name':josh,'level':dsan,'address':ichi,'department':sup} 

#  print(product) 
# n = []
# m = []
# val = int(input('Start'))
# val1 = int(input('Stop'))
# for x in range (val, val1) :
#  if (x % 2 == 0):
#      n.append(x)
#  else:
#      m.append(x)

# print(n)
# print(m)

# Cars = ["oau","futa","lau","ui"]
# for n in range(len(Cars)):
#  print(n,Cars,[n])
# person = ['paulou','bose','floa']
# # for n in range(1,len(person)):
# #     print(n,person[n])
# if 'paulou'


# val = int(input('Start'))
# val1 = int(input('Stop'))
# for x in range (val, val1, 2) :
#  print(x)
n = []
val = int(input('Start'))
val1 = int(input('Stop'))
for x in range (val, val1) :
 if (x % 7 == 0) and (x % 5 == 0 ):
   n.append(x)
   print(n)