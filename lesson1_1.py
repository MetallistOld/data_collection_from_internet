# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.
# https://api.github.com/users/USERNAME/repos

import requests
import time
import json


def get_data(url: str) -> dict:
    while True:
        time.sleep(1)
        response_git = requests.get(url)
        if response_git.status_code == 200:
            break
    return response_git.json()


username = input('Введите username: ')
username = 'MetallistOld' if username == '' else username
url = 'https://api.github.com/users/' + username + '/repos'

response = get_data(url)
print('Получен результат')

repo_list = []
for itm in response:
    repo_list.append(itm['name'])
print(f'Список репозиториев пользователя {username}')
print(repo_list)

with open('1_1_repo.json', 'w') as f:
    json_repo = json.dump(repo_list, f)
