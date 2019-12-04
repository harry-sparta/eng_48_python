# Functions
# A function is like a machine. It needs to be turned on and it does things.
# Good practice
    # They should be small and only do one job
        # avoid string code
        # testable code
        # maintainable code
        # readable
    # DRY (Don't Repeat Yourself)
    # Separation of concerns
        # - define functions in one file
        # - call them in another
        # - others
    # Do not print inside a function. Unless it is a print function
        # Call the function inside print()
# Functions work this way:
    # 1) Define function
    # 2) Call function
    # 3) Return if wished to
# Syntax
# def <name> (arg, arg2, arg3):
    # block
    # return something if you wish

# def say_hello():
#     return 'Hellooooo'
#
# print(say_hello())

def say_hello_user(f_name='first name', l_name='last name'):
    return 'Hello ' + f_name.capitalize() + ' ' + l_name.capitalize()

# print(say_hello_user())
# print(say_hello_user('bob', 'marley'))