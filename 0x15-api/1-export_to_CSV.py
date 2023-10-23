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
    status = [task.get("completed") for task in todos]
    todo_titles = [title.get("title") for title in todos]

    rows = zip([ID] * len(todo_titles), [user_name] * len(todo_titles), status, todo_titles)

    with open(f"{ID}.csv", mode="w", newline="") as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        csv_writer.writerows(rows)

if __name__ == "__main__":
    main()
