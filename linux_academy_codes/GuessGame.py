import random
"""

"""

ran = random.randint(1,20)
print(">>>>>Guess The Number Game<<<<<<")
print("A number is generated between 1- 20")
print("Enter a number")

try:
    a = int(input())
except ValueError:
    print("Invalid Integer")
    a = int(input())  

print("The guessed number by player is: ",a)

i = 0
while i <= 4:
    if a < ran:
        print("Guess is low")
        a = int(input("Guess Again:"))
        i = i + 1 
        continue
    elif a > ran:
        print("Guess is High")
        a = int(input("Guess Again:"))
        i = i + 1
        continue
    else:
        print("You guessed it correctly")
    break       
print("The target number was :",ran)
