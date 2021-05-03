#!/usr/bin/python3
"""This module makes a request to a RESTful API."""
import requests
from sys import argv


if __name__ == "__main__":

    # Get employee name
    employee_id = int(argv[1])
    r = requests.get('https://jsonplaceholder.typicode.com/users')

    for dic in r.json():
        if dic.get('id') == employee_id:
            employee_name = dic.get('name')
            break

    # Get employee's tasks
    r = requests.get('https://jsonplaceholder.typicode.com/todos/')
    done = []
    total = 0
    tasks = r.json()
    for task in tasks:
        if task.get('userId') == employee_id:
            total += 1
            if task.get('completed') is True:
                done.append(task.get('title'))

    # Print in correct format
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done), total))
    for task in done:
        print("\t {}".format(task))
