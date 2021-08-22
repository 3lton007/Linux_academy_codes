
#Rock papar scissors
import random


print(" Rock \n Paper \n Scizzors")
user = input()

a = ['Rock','Paper','Scizzors']
comp= random.choice(a)
print(comp)


if (user =='Rock'  and comp =='Paper'):
    print("Comp wins")
   
elif (user =='Rock' and comp =='Scizzors'):
    print("User wins")


elif(user =='Paper' and comp =='Rock'):
    print("User wins")
    
elif (user =='Paper' and comp == 'Scizzors'):
    print("Comp Wins")
       

elif(user == 'Scizzors' and comp == 'Rock'):
    print("Comp wins")
     
elif (user == 'Scizzors' and comp == 'Paper'):
    print("User wins")

else:
    print("Its a draw")

    



