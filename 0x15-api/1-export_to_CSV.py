#!/usr/bin/python3
"""script to export data in the CSV format."""

import requests
import sys
import csv

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    employee_id = int(sys.argv[1])

    name_employee = requests.get(url + "users/{}".format(employee_id)).json()

    username = name_employee.get("username")

    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [employee_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
