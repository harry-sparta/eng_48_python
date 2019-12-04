# For loops with dictionaries
dict_data = {
    1: {
        'name': 'Bronson',
        'money': 0.50,
    },
    2: {
        'name': 'Janet',
        'money': 3.50,
    },
    3: {
        'name': 'Bartolumeu',
        'money': 1.50,
    },
    4: {
        'name': 'Bob',
        'money': 9.50,
    }
}

# When you do a simple for loop on a dictionary, you get the individual keys
# for key in dict_data:
#     print(key)
#     print(dict_data[key])

# for key in dict_data:
#     print(key, '-->', dict_data[key])

# We want the name of the person, how much they owe us and apply interest (4000% per annum)
# for key in dict_data:
#     print(dict_data[key]['name'], 'owes us', (dict_data[key]['money']*400/12+dict_data[key]['money']))


for values in dict_data.values():
    print(values)