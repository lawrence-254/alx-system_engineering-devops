#!/usr/bin/python3
'''Python script that returns information aboutTODO list progress.'''
import csv
import requests
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python todo_progress.py ID")
        sys.exit(1)

    ID = int(sys.argv[1])
    if not isinstance(ID, int):
        print("ID must be an integer")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com/"
    employee_data = requests.get(base_url + f"users/{ID}").json()
    todos = requests.get(base_url + "todos", params={"userId": ID}).json()

    user_name = employee_data.get("username")
    '''json'''
    todo_list = []
    for todo in todos:
        status = todo.get("completed")
        todo_title = todo.get("title")
        desc = {
                "task": todo_title,
                "completed": status,
                "username": user_name
                }
        todo_list.append(desc}
    data = {str(ID): todo_list}

    with open(f"{ID}.json", mode="w", newline="") as file:
        json.dump(data, file)


if __name__ == "__main__":
    main()
