#!/usr/bin/python3
"""This module makes a request to a RESTful API."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        exit

    # Get list of user IDs
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    users_dic = r.json()
    users_list = []
    master_dic = {}
    for user in users_dic:
        user_id = user.get('id')
        users_list.append(user_id)
        username = user.get('username')
        # Create list of tasks for each user and append to new dict
        for user_id in users_list:
            task_list = []
            t = requests.get('https://jsonplaceholder.typicode'
                             '.com/users/' + str(user_id) + '/todos')
            for task in t.json():
                task_info = {}
                task_info["username"] = username
                task_info["task"] = task.get('title')
                task_info["completed"] = task.get('completed')
                task_list.append(task_info)
        # Append user list of tasks to master dictionary
        master_dic[user_id] = task_list

    with open("todo_all_employees.json", "w") as f:
        json.dump(master_dic, f)
