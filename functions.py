import requests

url = 'https://jsonplaceholder.typicode.com/todos'


def fetch_todos_online():
    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        return []


def get_first_20_even_todos(todos):
    even_todos_list = []
    even_count = 0
    for todo in todos:
        if even_count < 20:
            # I'm using 'id' field indicates the numbering of TODOs. I'm filtering all id's which are even.
            if todo['id'] % 2 == 0:
                even_count = even_count +1
                even_todos_list.append(todo)
        else:
            break
    return even_todos_list


def print_todo_titles(todos):
    for index, todo in enumerate(todos):
        print(f'{index + 1}. Title: {todo.get("title", "")} \nStatus: {todo.get("completed", "")}\n ')