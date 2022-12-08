import random
print("__________Lets play a game__________\nI'm thinking of a number between 0 and 10\nLets see if you are wise enough to guess the correct number\nyou only get three chances\n\nLets goo")
randon_num = random.randint(0,10)
inpu = int(input("Enter your first guess:"))
if inpu == randon_num:
    print("Correct")
else:
    print("Incorrect")
    inpu2 = int(input("Enter your second guess:"))
    if inpu2 == randon_num:
        print("Correct")                 
    else:
        print("Incorrect")
        inpu3 = int(input("Enter your last guess:"))
        if inpu3 == randon_num:
            print("Correct")
        else:
            print("Thats too bad")
            print(f"The correct number is {randon_num}")