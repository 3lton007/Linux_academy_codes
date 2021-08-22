
#The while loop

"""
The while loop are simple type of loops to repeat
something again and again, till the condition is met
"""

"""
count = 1
while ( count <= 4):
     print ("looping")
     count += 1
"""


count = 0 
while count <= 10 :
    if count % 2 == 0:
        count += 1
        continue
    print(f"The odd nos are: {count}")    
    count += 1


"""
count = 0
while count <= 10:
    if count % 2 == 1:
        print(" the odd nos :" , count )
    count += 1
"""        
        