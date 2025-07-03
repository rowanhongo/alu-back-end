#!/usr/bin/python3
""" Import libraries """

import sys
import urllib.request
import json

"""Gathering data from an API """

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    with urllib.request.urlopen(url) as response:
        user_info = json.loads(response.read().decode())

    with urllib.request.urlopen(todo_url) as response:
        todo_info = json.loads(response.read().decode())

    employee_name = user_info.get("name")
    completed_tasks = list(filter(lambda x: x.get("completed") is True, todo_info))
    number_done = len(completed_tasks)
    total_tasks = len(todo_info)

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          number_done, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
