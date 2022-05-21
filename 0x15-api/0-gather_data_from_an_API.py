#!/usr/bin/python3
"""Python script that, using a REST API, for a given
    employee ID, returns information about
    his/her TODO list progress."""

import requests
from sys import argv

if __name__ == "__main__":
    payload = {"userId": argv[1]}
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get('{}users/{}'.format(url, argv[1])).json()
    todos = requests.get('{}todos/'.format(url), params=payload).json()

    total = len(todos)
    done = 0
    tasks = []

    for i in todos:
        if i.get('completed') is True:
            done += 1
            tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        users.get('name'), done, total))

    for task in tasks:
        print("\t {}".format(task))
