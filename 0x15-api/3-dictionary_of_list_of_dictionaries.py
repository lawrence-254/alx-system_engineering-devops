#!/usr/bin/python3
'''Python script that returns information aboutTODO list progress.'''
import json
import requests


def main():
    base_url = "https://jsonplaceholder.typicode.com/"
    total_employee_data = requests.get(base_url + "users").json()
    todos = requests.get(base_url + "todos").json()
    data = {}

    for employee_data in total_employee_data:
        user_id = employee_data.get("id")
        user_name = employee_data.get("username")
        todo_list = []

        for todo in todos:
            assoc_id = todo.get("userId")
            status = todo.get("completed")
            todo_title = todo.get("title")
            if user_id == assoc_id:
                desc = {
                        "task": todo_title,
                        "completed": status,
                        "username": user_name
                        }
                todo_list.append(desc)
            data[str(assoc_id)] = todo_list

    with open("todo_all_employees.json", mode="w", newline="") as file:
        json.dump(data, file)


if __name__ == "__main__":
    main()
