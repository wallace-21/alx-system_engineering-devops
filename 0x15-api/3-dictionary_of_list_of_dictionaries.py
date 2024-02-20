#!/usr/bin/python3
"""Python script to export data in the JSON format."""

import json
import requests


def fetch_user_data():
    """Fetches user data"""
    url = "https://jsonplaceholder.typicode.com/"

    name_employee = requests.get(url + "users").json()

    data = {}
    for user in name_employee:
        employee_id = user["id"]
        user_url = url + "todos?userId={}".format(employee_id)
        todo_list = requests.get(user_url).json()

        data[employee_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username"),
            }
            for todo in todo_list
        ]

    return (data)


if __name__ == "__main__":

    data = fetch_user_data()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
