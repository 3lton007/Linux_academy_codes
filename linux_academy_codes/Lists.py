
#Learning Lists and Its Methods

my_list = [1,2,3,4,5]
print(my_list)

print(my_list[0])

print(my_list[3])

print(len(my_list))


#SLICING

print(my_list[0:2])  # It is [Index start point , Index End point]..the Endpoint wont be included

print(my_list[2:4])  # This will print the index 2 and 3

print(my_list[:4])   # It assumes the starting point index is 0 ( prints index 0,1,2,3)


#Three step list

#This makes use of three steps ie. [start:end:step]
#step is used to print perodic numbers

print(my_list[::2])   # This prints the starting index value and then does the step value assigned to it.

print(my_list[::3])   #THis prints index value and jumps to 4th value.

print(my_list[::-1])  # Using a negative no. REVERSES the list.

print(my_list[::-2])  # List will be backwards and step 2 assigned to it.



#Modifying the list (Modify, insert, pop..etc) using methods.

print(my_list)

my_list[0] = 'a'
print(my_list)

my_list[0:2] = 'a'   #The list will take 2 items and replace it with the string 'a'
print(my_list)      

my_list[0:2] = [1,2,3]  #Used to revert Back
print(my_list)

my_list[3:4] = []    #As end index does not get included, item after the starting index is dicarded.
print(my_list)

"""
Using Methods with list using (.)
Some of the methods are :-

1)remove 2)append 3)clear 4)copy 5)insert 6)
"""