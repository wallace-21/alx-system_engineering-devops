#!/usr/bin/python3
"""extend your Python script to export data in the JSON format."""

import json
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    employee_id = int(sys.argv[1])

    name_employee = requests.get(url + "users/{}".format(employee_id)).json()

    username = name_employee.get("username")

    params = {"userId": employee_id}

    todos = requests.get(url + "todos", params).json()

    data = {
        employee_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump(data, jsonfile)
