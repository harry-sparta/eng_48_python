# Mr Miyagi project
# Ask for user input and depending on the response, mr Miyagi will respond.
    ## prompt user for input
    ## Evaluate each input and print the appropriate responses
    # Follow these rules:
        # - every time you ask a question --> Mr. Miyagi responds with
            # --> 'questions are wise, but for now. Wax on, and Wax off!'
        # - every statement/question must start with Sensei, otherwise:
            # --> 'You are smart, but not wise - address me as Sensei please'
        # - every time you mention 'block' or 'blocking' --> Mr. Miyagi responds with
            # --> 'Remember, best block, not to be there..'
        # - anything else you say:
            # --> 'do not lose focus. Wax on. Wax off.'
        # Make it so you keep playing until we say: 'Sensei, I am at peace'
            # --> 'Sometimes, what heart know, head forget'

question = ['?', 'who', 'why', 'when', 'what', 'how', 'where']
miyagi_response = {'sensei': 'You are smart, but not wise. Address me as Sensei please.',
                   'block': 'Remember, best block, not to be there.',
                   'question': 'Questions are wise, but for now, wax on and wax off.',
                   'ignore': 'do not lose focus. Wax on. Wax off.',
                   'bye': 'Sometimes, what heart know, head forget.',}

def question_detect (your_response_format):
    for object in question:
        if object in your_response_format:
            return True
        else:
            continue


while True:
    your_response = input('(MR.Miyagi)... -.-')
    your_response_format = your_response.strip().lower()
    if your_response_format[0:5] not in 'sensei':
        print(miyagi_response['sensei'])
    elif question_detect(your_response_format) == True:
        print(miyagi_response['question'])
    elif 'block' in your_response_format:
        print(miyagi_response['block'])
    elif 'sensei, i am at peace' in your_response_format:
        print(miyagi_response['bye'])
        break
    else:
        print(miyagi_response['ignore'])