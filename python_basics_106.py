# Nested data ion list and dictionaries
# mix_list = ['strings', 98, ['more string', [1, 2, 'important']]]
# print(type(mix_list[2]))
# print(mix_list[2][1][2])
#
# internal_list = mix_list[2]
# print(internal_list[1][2])

### /////

embeded_dict = {
    'status': 'operational',
    'key1': ['car keys', 'boat keys', 'mansion keys', 'dog house keys'],
    'staff': {
        'Julio Cesar': {
            'name': 'Julio',
            'last_name': 'Cesar',
            'birth_date': 1979,
            'football_club': 'Flamengo_FC'
        },
        'Julia Venus': {
            'name': 'Julia',
            'last_name': 'Venus',
            'birth_date': 1969,
            'football_club': 'Cuba_FC'
        }
    }
}

# Print:
## - the boat keys and dog house keys
## - Inside the key 'staff', print the dictionary with the key 'Julio Cesar'
## - Inside the key 'Julia Venus', print the last name, brithdate and the football club
print(embeded_dict['key1'][1], embeded_dict['key1'][3])
print(embeded_dict['staff']['Julio Cesar'])
print(embeded_dict['staff']['Julia Venus']['last_name'],
    embeded_dict['staff']['Julia Venus']['birth_date'],
    embeded_dict['staff']['Julia Venus']['football_club'])