#!/usr/bin/python3
'''Python script that returns information aboutTODO list progress.'''
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

    total_todos = len(todos)
    done = [todo.get("title") for todo in todos
            if todo.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        (employee_json_data.get("name")), len(done), total_todos))

    [print("\t {}".format(task)) for task in done]
