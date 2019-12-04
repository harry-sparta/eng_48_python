# Dictionary
# AKA --> hashes or (confusingly) object
# It works like exactly like a dictionary
# It has key and values pairs
    # The key is the word you look up
    # The value is the meaning / value of the word

# Syntax
# {}
# dict = {'key': 'value'}
my_dictionary = {
'tissues': 'A disposable piece of absorbent paper.',
'baseball_bat': 'It is a bat made of wood to play baseball.'}

# Accessing or Re-assigning is with the key inside the []
print(my_dictionary['baseball_bat'])

my_dictionary['baseball_bat'] = 'Really, you are looking up two seperate words'

print(my_dictionary['baseball_bat'])
