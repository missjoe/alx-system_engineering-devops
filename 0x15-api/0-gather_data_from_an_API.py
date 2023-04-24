#!/usr/bin/python3

"""

Gather data from an API

"""

from sys import argv
import requests

if __name__ == "__main__":
    user_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(base_url + "users/{}".format(user_id)).json()
    tasks = requests.get(base_url + "todos", params={"userId": user_id}).json()

    completed_tasks = []
    for task in tasks:
        if task.get("completed"):
            completed_tasks.append(task.get("title"))

print("Employee {} is done with tasks({}/{}):".format(
    employee.get("name"), len(completed_tasks), len(tasks)))

for task in completed_tasks:
    print("\t {}".format(task))
