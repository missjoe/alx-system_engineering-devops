#!/usr/bin/python3
"""export data in the JSON format."""
import json
import requests
import sys


if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    todo_dict = {}
    for user in users:
        user_id = str(user['id'])
        todo_list = []
        for todo in todos:
            if todo['userId'] == user['id']:
                task = todo['title']
                completed = todo['completed']
                todo_list.append({
                    "username": user['username'],
                    "task": task,
                    "completed": completed
                })
        todo_dict[user_id] = todo_list

    with open('todo_all_employees.json', 'w') as f:
        json.dump(todo_dict, f)
