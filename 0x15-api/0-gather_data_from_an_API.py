#!/usr/bin/python3
"""Given an Employee ID, returns information
about his/her TODO list progress.
"""
import requests
from sys import argv


def display():
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        return

    employee_id = int(argv[1])

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    for user in users.json():
        if user.get('id') == employee_id:
            employee_name = user.get('name')
            break
    else:
        print("Employee with ID {} not found.".format(employee_id))
        return

    total_num_of_tasks = 0
    number_of_done_tasks = 0
    task_titles = []

    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    for todo in todos.json():
        if todo.get('userId') == employee_id:
            total_num_of_tasks += 1
            if todo.get('completed'):
                number_of_done_tasks += 1
                task_titles.append(todo.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, number_of_done_tasks, total_num_of_tasks))
    for task in task_titles:
        print("\t{}".format(task))


if __name__ == "__main__":
    display()
