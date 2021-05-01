from utils.functions.prompting_functions import *


menu_text = '''Welcome to MyToDos v.1.0!
- Press "m" to manage your current ToDos
- Press "c" to create a new ToDo
- Press "z" to erase all your ToDos
- Press "q" to quit
- Your input: '''

menu_dict = {
    'm': manage_todos,
    'c': create_new_todo,
    'z': factory_reset
}


def menu():
    menu_input = ''

    while menu_input != 'q':
        menu_input = input(menu_text)

        if menu_input == 'm' or menu_input == 'c' or menu_input == 'z':
            menu_dict[menu_input]()

        elif menu_input == 'q':
            pass

        else:
            print('\nPlease enter a valid input.\n')

    print('\nProgram Exited.')


def create_todos_table():  # This function must run at the start of the program. It creates the 'data.db' database which stores the user's ToDos
    with Cursor() as c:
        c.execute('CREATE TABLE IF NOT EXISTS todos(id int, contents text, done int)')


create_todos_table()
menu()
