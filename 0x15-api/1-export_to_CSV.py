#!/usr/bin/python3
'''Python script that returns information aboutTODO list progress.'''
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python todo_progress.py ID")
        sys.exit(1)

    ID = int(sys.argv[1])
    if not isinstance(ID, int):
        print("ID must be an integer")
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"
    employee_json_data = requests.get(url + "users/{}".format(ID)).json()
    todos = requests.get(url + "todos", params={"userId": ID}).json()

    user_name = employee_json_data.get("username")
    status = [task.get("completed") for task in todos]
    todo_title = [title.get("title") for title in todos]

    rows = zip([ID] * len(todo-title),
            [user_name] * len(todo-title), status, todo-title)

    with open(f"{ID}.csv", mode="w", newline="") as file:
        csv.writer(file, quoting=csv.QUOTE_ALL).writerows(rows)
