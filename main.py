from functions import fetch_todos_online, get_first_20_even_todos, print_todo_titles


def start_app():
    todos_list = fetch_todos_online()
    todos = get_first_20_even_todos(todos_list)
    print_todo_titles(todos)


if __name__ == "__main__":
    start_app()
