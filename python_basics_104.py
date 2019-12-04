# List in Python
# Lists are ordered by index
## AKA --> arrays or (confusingly) as objects in JS

# Syntax
# Declare lists using []
    # separate obejcts using ,
# var_list_name = [   0   ,   1   ,   2   ,  3   ]
crazy_x_landlords = ['Sr. Julio', 'Jane', 'Alfred', 'Marksons']

print(crazy_x_landlords)
print(type(crazy_x_landlords))

# How to access record number 3 in the list
print(crazy_x_landlords[2])

# Accessing other location
print(crazy_x_landlords[0])     # Access first record
print(crazy_x_landlords[-1])    # Access last record

# New list of places to live
places_to_live = ['California', 'Rio de Janeiro', 'Melbourne', 'Manchester', 'Singapore']
print(places_to_live)

# Reassign an index
places_to_live[3] = 'Hawaii'
print(places_to_live)

# a.append(object)
print(len(places_to_live))
places_to_live.append('LA')
print(len(places_to_live))

# a.insert(index, object)
places_to_live.insert(0, 'Lisboa')
print(places_to_live)

# a.pop(index)
# Removes from list at specific index
places_to_live.pop(3)
print(places_to_live)

# List slicing
    # used to manage lists

# prints from index to end of list
print(places_to_live[3:])
#prints from index to start of list
print(places_to_live[:3])

# Prints from specified index to second specified index (inclusive)
print (places_to_live[0:3])
print (places_to_live[1:3])

# skip slicing
list_exp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12 ,13, 14]
print(list_exp[0::3])
print(list_exp[0:10:3])
print(list_exp[::-1])

# Tuples
# Immutable lists
# Syntax
    # Defined using (object, object)

mortal_enemies = ('Mario', 'Sailormoon', 'MOON CAKE', 'Jerry', 'Berry')
print(type(mortal_enemies))

# If you try to re-assign, it will break
# mortal_enemies [0] = 'Goku'
# print(type(mortal_enemies))

# Example of creating amazing list for end of the world survival
list_of_kit = []

item_1 = input('What is your 1st item to keep?')
list.append(list_of_kit, item_1)
item_2 = input('What is your 2nd item to keep?')
list.append(list_of_kit, item_2)
item_3 = input('What is your 3rd item to keep?')
list.append(list_of_kit, item_3)

print ('Hey there partner! You have a nice list of stuff!')
print (list_of_kit)
