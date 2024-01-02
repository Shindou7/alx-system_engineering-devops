#!/usr/bin/python3
'''
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''
import requests
from sys import argv


def gather_data(employee_id):
    """Retrieve data from the API for a given employee ID"""
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch user data
    users_response = requests.get(users_url)
    users = users_response.json()

    employee_name = None

    for user in users:
        if user.get('id') == employee_id:
            employee_name = user.get('name')
            break

    if employee_name is None:
        print("Employee with ID {} not found.".format(employee_id))
        return

    # Fetch TODOs for the given employee ID
    todos_response = requests.get(todos_url, params={'userId': employee_id})
    todos = todos_response.json()

    # Process TODOs
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get('completed')]
    num_completed_tasks = len(completed_tasks)

    # Display information
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, num_completed_tasks, total_tasks))

    for task in completed_tasks:
        print("\t{}".format(task.get('title')))


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
    else:
        try:
            employee_id = int(argv[1])
            gather_data(employee_id)
        except ValueError:
            print("Invalid employee ID. Please provide a valid integer.")
