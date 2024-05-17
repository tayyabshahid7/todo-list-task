import unittest
from mock import patch
from functions import get_first_20_even_todos, print_todo_titles


class TestApp(unittest.TestCase):

    def setUp(self):
        self.mock_todos = [
            {'id': i, 'title': f'TODO {i}', 'completed': True}
            for i in range(1, 100)
        ]

    def test_get_first_20_even_todos(self):
        even_todos = get_first_20_even_todos(self.mock_todos)
        self.assertEqual(len(even_todos), 20)
        for todo in even_todos:
            self.assertEqual(todo['id'] % 2, 0)

    def test_get_first_20_even_todos_with_less_data(self):
        even_todos = get_first_20_even_todos(self.mock_todos[:25])
        self.assertEqual(len(even_todos), 12)  # Only 12 even IDs in the first 25 TODOs

    @patch('functions.print')
    def test_print_todo_titles(self, mock_print):
        print_todo_titles(self.mock_todos[:2])

    @patch('functions.fetch_todos_online')
    def test_start_app(self, mock_fetch_todos_online):
        mock_fetch_todos_online.return_value = self.mock_todos
        from main import start_app
        start_app()
        mock_fetch_todos_online.assert_called_once()


if __name__ == '__main__':
    unittest.main()
