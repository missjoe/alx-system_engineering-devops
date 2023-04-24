#!/usr/bin/python3

"""
Gather data from an API and export in JSON format
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(base_url + "users/{}".format(user_id)).json()
    tasks = requests.get(base_url + "todos", params={"userId": user_id}).json()

    completed_tasks = []
    for task in tasks:
        if task.get("completed"):
            completed_tasks.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee.get("username")
            })

    result = {employee.get("id"): completed_tasks}

    with open(f"{user_id}.json", "w") as f:
        json.dump(result, f)
