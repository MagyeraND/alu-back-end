#!/usr/bin/python3
"""Script that exports employee TODO list data to JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = int(sys.argv[1])

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get("{}/todos?userId={}".format(base_url, employee_id)).json()

    username = user.get("username")
    filename = "{}.json".format(employee_id)

    tasks_list = []
    for task in todos:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    with open(filename, "w") as jsonfile:
        json.dump({str(employee_id): tasks_list}, jsonfile)

