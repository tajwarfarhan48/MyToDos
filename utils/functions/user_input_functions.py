"""
INPUT FUNCTIONS - THEIR MAIN JOB IS TO PROCESS THE INPUT THAT WILL BE RECEIVED FROM THE USER
"""


def allow_specific_input(user_prompt, valid_inputs=None):  # Prevents invalid inputs when the program asks the user to select from a set of options. It takes a list of the allowed inputs as one of the parameters.
    if valid_inputs is None:
        valid_inputs = ['']  # This is the default value of the list of valid inputs

    user_input = input(f'\n{user_prompt}')

    while user_input not in valid_inputs:  # Does not allow the program to proceed unless the user types a valid input
        print('\nPlease enter a valid input. In case of entering IDs, please enter a number between 1 and 999 without decimals.\n')
        user_input = input(user_prompt)

    return user_input


def prevent_blank_input(user_prompt):  # Prevents blank inputs when the user is prompted to enter new information
    user_input = input(f'{user_prompt}')

    while user_input == '':
        print(f'\nYou cannot leave this field blank.')
        user_input = input(user_prompt)

    return user_input


def id_searcher(user_prompt):  # This is a special version of the 'allow_specific_input' function. It is only used when the user is asked to enter a unique ID.
    valid_inputs = ['x', *[i for i in range(1, 1000)]]
    user_input = input(f'\n{user_prompt}')

    while user_input not in valid_inputs:  # Does not allow the program to proceed unless the user types a valid input
        try:  # Checks whether the user typed an integer. This section will only run if the user does not enter an integer between 1 and 999, or the letter 'x'
            user_input = int(user_input)
        except ValueError:  # Runs when a non-valid non-integer is typed
            print('\nPlease enter a valid input. In case of unique IDs please enter a number between 1 and 999.\n')
            user_input = input(user_prompt)
        else:  # Runs when an integer is typed
            if user_input in valid_inputs:
                pass
            else:  # Runs when a non-valid integer is typed
                print('\nPlease enter a valid input. In case of unique IDs please enter a number between 1 and 999.\n')
                user_input = input(user_prompt)

    return user_input
