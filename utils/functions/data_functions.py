import random
from utils.classes.Cursor import *
from utils.classes.ToDo import *


'''
DATA FUNCTIONS - THEIR MAIN JOB OF THESE FUNCTIONS IS TO RETRIEVE AND WRITE DATA TO THE DATABASE
'''


def fetch_all_stored_todos():  # Returns a list of all the ToDos saved by the user. Each ToDo is an instance of the ToDo class.
    with Cursor() as c:
        c.execute('SELECT * FROM todos')
        stored_rows = c.fetchall()

    stored_todos = [ToDo(*row) for row in stored_rows]  # Each row is in the format: (ID, contents, done)

    return stored_todos


def fetch_all_occupied_ids():  # Returns a list of the IDs of the ToDos saved by the user. Mainly used for searching purposes when a user wants to interact with a ToDo
    occupied_ids = [todo.id for todo in fetch_all_stored_todos()]
    return occupied_ids


def save_to_table(todo):  # For saving a ToDo to the database
    with Cursor() as c:
        c.execute(f'INSERT INTO todos VALUES(?, ?, ?)', (todo.id, todo.contents, todo.done))

    print('\nYour ToDo has been saved.\n')


def remove_from_table(todo_id):  # For removing a ToDo from the database
    with Cursor() as c:
        c.execute(f'DELETE FROM todos WHERE id=?', (todo_id,))

    print('\nThe ToDo has been removed.\n')


def mark_as_done(todo_id):  # Changes the status of a ToDo to 'Done' in the database
    with Cursor() as c:
        c.execute('UPDATE todos SET done=1 WHERE id=?', (todo_id,))

    print('\nThe ToDo has been marked as Done.\n')


def generate_id():  # Generates a random, unique ID for each ToDo. The user has to use the ID of the ToDo in order to interact with it.
    todo_id = random.randint(1, 999)
    occupied_ids = fetch_all_occupied_ids()

    while todo_id in occupied_ids:
        todo_id = random.randint(1, 999)

    return todo_id


def view_all_todos():  # Views all the user's ToDos
    stored_todos = fetch_all_stored_todos()
    incomplete_todos = [todo for todo in stored_todos if todo.done == 0]
    complete_todos = [todo for todo in stored_todos if todo.done == 1]

    if len(stored_todos) == 0:  # Runs when the user has no stored ToDos
        print('\nYou currently have no ToDos')
        return None

    print('\nYour ToDos are:')

    for todo in incomplete_todos:
        print(f'\nID: {todo.id} - {todo.contents} - Status: X')

    for todo in complete_todos:
        print(f'\nID: {todo.id} - {todo.contents} - Status: √')
