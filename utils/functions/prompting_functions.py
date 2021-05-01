from utils.functions.user_input_functions import *
from utils.functions.data_functions import *

'''
PROMPTING FUNCTIONS - THEY LINK THE INPUT FUNCTIONS TO THE DATA FUNCTIONS
'''


def create_new_todo():  # Runs when the user wants to add a new ToDo
    user_input = prevent_blank_input('\nEnter your todo here. Press x to cancel: ')

    if user_input == 'x':  # Cancels the action
        print('')
        return None

    new_todo = ToDo(generate_id(), user_input, 0)
    save_to_table(new_todo)


def manage_todos():  # Runs when the user wants to manage their ToDos
    view_all_todos()

    user_input = allow_specific_input('Press d to delete a ToDo. Press c to mark a ToDo as complete. Press x to return to main menu: ', ['d', 'c', 'x'])  # Prompts the user to either return to the main menu, or to mark a ToDo as Done, or delete a ToDo

    if user_input == 'x':
        print('')
        return None

    elif user_input == 'd':
        delete_todo_prompt()

    elif user_input == 'c':
        mark_todo_as_complete_prompt()


def delete_todo_prompt():  # Runs when the user wants to delete a ToDo
    user_input = id_searcher('Enter the unique ID of the ToDo you wish to delete (between 1 and 999). Press x to cancel: ')

    if user_input == 'x':
        print('')
        return None

    if user_input not in fetch_all_occupied_ids():
        print('\nThere is no ToDo with the entered ID.\n')

    else:
        remove_from_table(user_input)


def mark_todo_as_complete_prompt():  # Runs when the user wants to mark a ToDo as Done
    user_input = id_searcher('Enter the unique ID of the ToDo you wish to mark as complete (between 1 and 999). Press x to cancel: ')

    if user_input == 'x':
        print('')
        return None

    if user_input not in fetch_all_occupied_ids():
        print('\nThere is no ToDo with the entered ID.\n')

    else:
        mark_as_done(user_input)


def factory_reset():  # Resets the ToDo list by deleting all the data from the 'data.db' database
    user_input = input('\nThis action is irreversible. Do you want to proceed? (press y for yes): ')

    if user_input == 'y':
        with Cursor() as c:
            c.execute('DELETE FROM todos')

        print('\nYour ToDos have been deleted.\n')

    else:
        print('')
