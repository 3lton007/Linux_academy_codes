
#Learning For Loop

color = ['blue' , 'green' , 'yellow' , 'red']

for sprinkles in color:
    print(sprinkles)

for satyug in color:
    if color == 'blue':
        continue
    elif color == 'red':
        break
    print(f" colors:{satyug}")
    

ages =  {'kevin' : 20 , 'Elton' : 20 , 'Naruto' : 20}

for i in ages:
    print(f" Name : {i} , Age : {ages[i]} ")


a = "my_string"
for letter in a:
    print(letter)

list_points = [(1,2) , (2,4) , (3,6)]
for x,y in list_points:
    print(f"x : {x} , y: {y}")



