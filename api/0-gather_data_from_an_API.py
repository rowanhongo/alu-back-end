#!/usr/bin/python3
"""Fetch and display an employee's TODO list progress from JSONPlaceholder"""

import requests
import sys

if __name__ == "__main__":
    # Ensure only 1 argument is passed
    if len(sys.argv) != 2:
        sys.exit()

    employee_id = sys.argv[1]

    # Fetch user info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    employee_name = user_data.get("name")

    # Fetch todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todos_data if task.get("completed")]

    # Print result in the exact expected format
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, len(completed_tasks), len(todos_data)
        )
    )
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
