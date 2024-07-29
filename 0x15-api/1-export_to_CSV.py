#!/usr/bin/python3
"""
Module: 0-gather_data_from_an_API
Description: Export api to csv
"""
import csv
import requests
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/' + user
    res = requests.get(user)
    """ANYTHING"""
    user_name = res.json().get('username')
    task = url + '/todos'
    res = requests.get(task)
    tasks = res.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            """Complete"""
            title_task = task.get('title')
            """Done"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_task))
