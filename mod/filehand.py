# import os
# files = os.path.exists()
# myfile = open("C:\\Users\\USER\\Desktop\\pyton\\mod\\fil3.py", "rb")
# print(myfile.read())
import os
py = []
oth = []

for root, dirs, files in os.walk("C:\\Users\\USER\\Videos\\"):
     for file in files:
        if file.endswith(".mp4"):
           py.append(file)
        else:
           oth.append(file)
# print(len(name2))
print(py)