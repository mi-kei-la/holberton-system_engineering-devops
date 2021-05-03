#!/usr/bin/python3
"""This module makes a request to a RESTful API."""
import requests
from sys import argv
import json


if len(argv) < 2:
    exit

# Get employee name
employee_id = int(argv[1])
par = {'id': str(employee_id)}
r = requests.get('https://jsonplaceholder.typicode.com/users', params=par)

for dic in r.json():
    if dic.get('id') == employee_id:
        employee_name = dic.get('name')
        username = dic.get('username')

# Get employee's tasks
par = {'userId': str(employee_id)}
r = requests.get('https://jsonplaceholder.typicode.com/todos', params=par)
done = []
tasks = r.json()
total = len(tasks)
for task in tasks:
    if task.get('completed') is True:
        done.append(task.get('title'))

# Print in correct format
print("Employee {} is done with tasks ({}/{}):".format(
      employee_name, len(done), total))
for task in done:
    print("\t {}".format(task))

# Serialize to JSON file
filename = argv[1] + '.json'
task_list = []
for task in tasks:
    new_task = {}
    new_task["task"] = task.get('title')
    new_task["completed"] = task.get('completed')
    new_task["username"] = username
    task_list.append(new_task)
j_obj = {employee_id: task_list}

with open(filename, "w") as f:
    json.dump(j_obj, f)
