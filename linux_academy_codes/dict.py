"""
#Learning Dictionaries 

ages = {'kevin' : 27 , 'Adith' : 23 , 'Elton' : 21}
print(ages)

ages['keith'] = 30
print(ages)


del ages
print(ages)

#To pop item between dict
ages.pop('Elton')
print(ages)

#To get value of item
print(ages.get('kevin'))

#To get keys
print(ages.keys())

#To get value of keys
print(ages.values())

#MAKE YOUR OWNNNN DICTIONARYYY

weights = dict(kevin=150, bob=120)
print(weights)

colors = dict([('kevin','blue') , ('bob','green')])
print(colors)

"""

ages = {'Elton' : 20 , 'Naruto' : 15, 'Sasuke' : 32}
for name,Age in ages.items():
    print(f"Person name is : {name}")
    print(f"Age in {Age}")