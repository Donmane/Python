from playerb import Player as player
import sys 
pla = player()
inp = input("Enter:")
if inp == "Video":
 print(pla.video())
elif inp == "Audio":
   print(pla.audio())
elif inp == "CSS":
   print(pla.css())
elif inp == "Javascript":
   print(pla.java())
elif inp == "HTML":
   print(pla.html())
elif inp == "Python":
   print(pla.python())
else:
   print("There are no files here")
   sys.exit()