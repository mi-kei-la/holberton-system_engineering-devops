#!/usr/bin/python3
""" This module makes a request to a RESTful API
and exports the pertinent data to a CSV file.
"""
from sys import argv
import csv
import requests

if __name__ == "__main__":
    if len(argv) < 2:
        exit

    # Get employee name
    emp_id = int(argv[1])
    par = {'id': str(emp_id)}
    r = requests.get('https://jsonplaceholder.typicode.com/users', params=par)

    for dic in r.json():
        if dic.get('id') == emp_id:
            emp_name = dic.get('name')
            username = dic.get('username')

    # Get employee's tasks
    par = {'userId': str(emp_id)}
    r = requests.get('https://jsonplaceholder.typicode.com/todos', params=par)
    done = []
    tasks = r.json()
    total = len(tasks)
    for task in tasks:
        if task.get('completed') is True:
            done.append(task.get('title'))

    # Print in correct format
    print("Employee {} is done with tasks ({}/{}):".format(
        emp_name, len(done), total))
    for task in done:
        print("\t {}".format(task))

    # Export to CSV
    filename = argv[1] + '.csv'
    with open(filename, mode='w') as f:
        f = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for task in tasks:
            status = task.get('completed')
            title = task.get('title')
            f.writerow([emp_id, username, status, title])
