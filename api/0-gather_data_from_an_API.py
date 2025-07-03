#!/usr/bin/python3
"""Script to gather TODO list progress of an employee from an API"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Get user info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    
    if user_response.status_code != 200:
        print("User not found.")
        sys.exit(1)

    user_info = user_response.json()
    employee_name = user_info.get("name")

    # Get todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Count completed tasks
    completed_tasks = [task for task in todos if task.get("completed") is True]
    total_done = len(completed_tasks)
    total_tasks = len(todos)

    # Output
    print(f"Employee {employee_name} is done with tasks({total_done}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
