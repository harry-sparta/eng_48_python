# While loops
# Syntax
# while <condition>:
    # block of code
    # block of code
    # condition
        # Break

# Basic while loop
# num = 0
# while num < 10:
#     print('still less than 10')
#     num += 1


# Using while loop to substitute the for loop from 108
# wish_list = ['rc car', 'molten cheese','cheerleaders', 'white shirts',
#              'sugar laces', 'reeses pieces', 'pasteis de nata']

# print(len(wish_list))
# index_length = len(wish_list)-1
#
# counter = 0
# while counter <= index_length:
#     print(wish_list[counter])
#     counter += 1

# Magic number game with breakpoint
# While loop with if statement and breakpoint clause
while True:
    # generate and random number
    num = 14
    # ask for user input
    user_guess = int(input('What number do you think I am thinking of?'))
    # evaluate input and respond appropriately
    if num == user_guess:
        print('Wholy cow! You guessed it!')
    elif user_guess > num:
        print('Lower ... bit lower!')
    elif user_guess < num:
        print('higher, bit higher')
    elif num == 0:
        breakpoint()
