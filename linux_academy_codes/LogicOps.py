
"""
Logic Operators
1) OR 2)AND 3)NOT

"""
#1)OR If First is True, it wont check the 2nd criteria . This is called Short Circuiting

print("" or 'Keith')

print('Keith' or 0 )

first = ''
last = 'Aloys'

if (first or last):
    print("The user has a part of name")


#2)AND - Checks for both and then decides


first = 'Elton'
last = ''

if (first and last):
    print("User has a name")

print('' and 'Keith')

print('Keith' and '')


#3)NOT

print(bool(not('')))

print(bool(not 1 > 2))

if not 1 > 2 :
    print("no it isnt")

