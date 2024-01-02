#!/usr/bin/python3
'''
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''
import requests
from sys import argv

def display(employee_id):
    # Fetch user data
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    user_data = next((user for user in users.json() if user.get('id') == employee_id), None)

    if user_data is None:
        print(f"Error: Employee with ID {employee_id} not found.")
        return

    EMPLOYEE_NAME = user_data.get('name')

    # Fetch TODO data
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_todos = [todo for todo in todos.json() if todo.get('userId') == employee_id]

    TOTAL_NUM_OF_TASKS = len(user_todos)
    NUMBER_OF_DONE_TASKS = sum(1 for todo in user_todos if todo.get('completed'))
    TASK_TITLE = [todo.get('title') for todo in user_todos if todo.get('completed')]

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUM_OF_TASKS))
    
    for task in TASK_TITLE:
        print("\t {}".format(task))

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python 0-gather_data_from_an_API.py <Employee_ID>")
        exit()

    try:
        employee_id = int(argv[1])
    except ValueError:
        print("Error: Invalid Employee ID")
        exit()

    display(employee_id)
