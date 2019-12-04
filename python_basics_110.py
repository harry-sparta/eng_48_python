# If functions
# Control flow
# While loops are also part of control flow
# Syntax
# if <condition> :
    # block of code
# elif <condition>
    # block of code
# else:
    # block of code

age = int(input('How old are you?'))

if age < 21 and age >= 18 :
    print('Sorry you can vote but not drink.')
elif age >= 21:
    print('You can vote, drink and drive.')
elif age >= 16:
    print('You can drive in the US but not vote or drink.')
else:
    print('You are a child.')

# Most specific has to be on top
# Conditions are built with operators and logical operators
# Once something is True, the block runs
