#!/usr/bin/python3
"""Python script that, using a REST API, for a given
    employee ID, returns information about 
    his/her TODO list progress."""

import requests
from sys import argv

if __name__ == "__main__":
    
    payload = {"userId": argv[1]}
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos/', params=payload).json()

    total = len(todos)
    completed = 0
    tasks = []

    for i in todos:
        if i.get('completed') is True:
            completed += 1
            tasks.append(i.get('title'))

    print("Employee {} is done with ({}/{}).".format(users.get('name'), completed, total))
    
    for task in tasks:
        print("\t{}".format(task))
