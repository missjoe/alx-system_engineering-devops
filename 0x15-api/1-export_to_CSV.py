#!/usr/bin/python3

"""
Gather data from an API and export to CSV
"""

import csv
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
                "userId": user_id,
                "username": employee.get("username"),
                "completed": str(task.get("completed")),
                "title": task.get("title")
            })

    csv_filename = "{}.csv".format(user_id)
    with open(csv_filename, "w", newline='') as csvfile:
        fieldnames = ["userId", "username", "completed", "title"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in completed_tasks:
            writer.writerow(task)

    print("Exported {} tasks to {}".format(len(completed_tasks), csv_filename))
