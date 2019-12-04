# Strings


## Define string using ' ' and " "
my_string = "I'm an amazing string"
my_string2 = 'I am'
my_name = 'a Potato'

print(my_string)
print(type(my_string2))


# Concatenation - Joining of two string
print ('this is an example of concatenation: ' + my_string)
print('these are examples of strings', my_string2, my_string)

concatenate = my_string2 + ' ' + my_name
print(concatenate)


# Interpolation
age = 21
name = 'Julia'

# This is where we need to interpolate
print('Welcome <person>, you are <age_years> old')
print('Welcome <person>, you were born on the year <date_birth>')

# This is us actually interpolating values
# Using standard formatting method
print('Welcome {}, you were born the year {}'.format(name, age))

# Using f shortcut formatting
print(f'Welcome {name}, you are {age} old')
print(f'Welcome {name}, you were born on the year {2019 - age}')



## Useful method for strings
example_string = "   hello    "
print(example_string)
print(example_string.strip()) # Remove trailing white spaces
print(example_string.count('l')) # Count number of characters on string
print(example_string.lower())
print(example_string.upper())
print(example_string.strip().capitalize()) # chaining methods

# Learning and using .split()
#
text_to_split = 'this is some example text in our file'
results_split = text_to_split.split(' ')
print(results_split)

# Standard builtin function len()
print(len(example_string))


# Casting and int
str_string = '1990'
print(type(str_string))

# Casting str --> int
int_number = int(str_string)
print(type(int_number))

# Casting int --> str
new_str = str(int_number)
print(type(new_str))