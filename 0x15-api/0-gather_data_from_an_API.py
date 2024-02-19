#!/usr/bin/python3
""" A Python script that, using this REST API,
for a given employee ID
returns information about his/her TODO list progress
"""

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = int(sys.argv[1])
    name_of_employee = requests.get(url + "users/{}".format(employee_id)).json()

    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params=params).json()

    completed_tasks = [t.get("title") for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        name_of_employee.get("name"), len(completed_tasks), len(todos)))

    [print("\t {}".format(complete)) for complete in completed_tasks]
