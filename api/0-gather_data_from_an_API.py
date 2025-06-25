#!/usr/bin/python3
"""
This is a script that fetches Employee data from jsonplaceholder REST API according to the employee ID entered.

This script retrieves employee data and their Todo tasks by employee ID
and prints the completion status and titles of completed tasks.
"""

import requests

User_input = input("Hello, Enter the employee ID in number form from 1 to 10: ")
User_id = int(User_input)

if User_id in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print("Checking status....")

    Employee_URL = f"https://jsonplaceholder.typicode.com/users/{User_id}"
    ToDo_URL = f"https://jsonplaceholder.typicode.com/todos?userId={User_id}"

    response1 = requests.get(Employee_URL)
    response2 = requests.get(ToDo_URL)

    if response1.status_code == 200 and response2.status_code == 200:
        data1 = response1.json()
        data2 = response2.json()

        EMPLOYEE_NAME = data1["name"]
        NUMBER_OF_DONE_TASKS = sum(1 for task in data2 if task["completed"] == True)
        TOTAL_NUMBER_OF_TASKS = len(data2)

        print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

        for task in data2:
            if task["completed"] == True:
                print(f"\t {task['title']}")
    else:
        print("Failed")
else:
    print("Wrong option entered")
