#!/usr/bin/python3
""" Python script to export data in the CSV format."""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    employee = argv[1]
    payload = {"userId": employee}
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get('{}users/{}'.format(url, argv[1])).json()
    todos = requests.get('{}todos/'.format(url), params=payload).json()

with open("{}.csv".format(employee), 'w') as f:
    csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    for i in todos:
        status = i.get('completed')
        task = i.get('title')
        csv_writer.writerow([employee, users.get("username"), status, task])
